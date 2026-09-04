from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).parents[2]
GOOD_REVISION = "a" * 40
TAG_OBJECT = "b" * 40
OTHER_REPOSITORY_REVISION = "c" * 40


class _ReleaseAsset(TypedDict):
    name: str
    size: int
    state: str
    url: str


class _PublicationAsset(TypedDict):
    name: str
    size_bytes: int
    sha256: str
    manifest: str
    url: str


def test_verifier_rejects_tag_from_a_different_repository(tmp_path: Path) -> None:
    manifests = tmp_path / "manifests"
    assets = tmp_path / "assets"
    fake_bin = tmp_path / "bin"
    manifests.mkdir()
    assets.mkdir()
    fake_bin.mkdir()
    release_assets: list[_ReleaseAsset] = []
    publication_assets: list[_PublicationAsset] = []
    for index in range(4):
        name = f"raw-{index}.tar.gz"
        body = f"asset-{index}".encode()
        _ = (assets / name).write_bytes(body)
        digest = hashlib.sha256(body).hexdigest()
        manifest = manifests / f"raw-{index}-manifest.json"
        _ = manifest.write_text(
            json.dumps(
                {
                    "revision": GOOD_REVISION,
                    "archive_name": name,
                    "archive_size_bytes": len(body),
                    "archive_sha256": digest,
                }
            ),
            encoding="utf-8",
        )
        url = f"https://example.invalid/{name}"
        release_assets.append({"name": name, "size": len(body), "state": "uploaded", "url": url})
        publication_assets.append(
            {
                "name": name,
                "size_bytes": len(body),
                "sha256": digest,
                "manifest": str(manifest),
                "url": url,
            }
        )
    release_url = "https://example.invalid/releases/item7"
    published_at = "2026-09-04T00:00:00Z"
    release = tmp_path / "release.json"
    _ = release.write_text(
        json.dumps(
            {
                "tagName": "item7-test",
                "url": release_url,
                "isDraft": False,
                "isPrerelease": False,
                "publishedAt": published_at,
                "assets": release_assets,
            }
        ),
        encoding="utf-8",
    )
    publication = tmp_path / "publication.json"
    _ = publication.write_text(
        json.dumps(
            {
                "schema_version": "item7-raw-evidence-publication-v1",
                "repository": "other/repository",
                "tag": "item7-test",
                "tag_object_sha": TAG_OBJECT,
                "source_revision": GOOD_REVISION,
                "release_url": release_url,
                "published_at": published_at,
                "downloaded_bytes_verified": True,
                "assets": publication_assets,
            }
        ),
        encoding="utf-8",
    )
    _write_fake_git(fake_bin / "git")
    _write_fake_gh(fake_bin / "gh")
    download = tmp_path / "download"
    environment = os.environ.copy()
    environment.update(
        {
            "PATH": f"{fake_bin}:{environment['PATH']}",
            "FAKE_ASSETS": str(assets),
            "FAKE_RELEASE": str(release),
            "FAKE_GIT_CALLED": str(tmp_path / "git-called"),
        }
    )

    result = subprocess.run(  # noqa: S603 - fixed repository verifier.
        [  # noqa: S607 - bash resolves within the controlled test environment.
            "bash",
            str(ROOT / "tools/verify_item7_release.sh"),
            "other/repository",
            "item7-test",
            str(manifests),
            str(publication),
            str(download),
        ],
        cwd=ROOT,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "remote tag does not resolve to the archive revision" in result.stderr
    assert not download.exists()
    assert not (tmp_path / "git-called").exists()


def _write_fake_git(path: Path) -> None:
    _ = path.write_text(
        "".join(
            (
                "#!/usr/bin/env bash\n",
                "printf 'called\\n' > \"$FAKE_GIT_CALLED\"\n",
                f"if [[ $* == *'^{{}}'* ]]; then printf '%s\\n' '{GOOD_REVISION}'; ",
                f"else printf '%s\\n' '{TAG_OBJECT}'; fi\n",
            )
        ),
        encoding="utf-8",
    )
    path.chmod(0o755)


def _write_fake_gh(path: Path) -> None:
    tag_response = json.dumps({"object": {"type": "commit", "sha": OTHER_REPOSITORY_REVISION}})
    _ = path.write_text(
        "".join(
            (
                "#!/usr/bin/env bash\n",
                "set -euo pipefail\n",
                "if [[ $1 == api ]]; then\n",
                f"  printf '%s\\n' '{tag_response}'\n",
                "elif [[ $1 == release && $2 == view ]]; then\n",
                '  cat "$FAKE_RELEASE"\n',
                "elif [[ $1 == release && $2 == download ]]; then\n",
                "  while [[ $# -gt 0 ]]; do\n",
                "    if [[ $1 == --dir ]]; then shift; destination=$1; fi\n",
                "    shift\n",
                "  done\n",
                '  cp "$FAKE_ASSETS"/* "$destination"/\n',
                "else\n",
                "  exit 2\n",
                "fi\n",
            )
        ),
        encoding="utf-8",
    )
    path.chmod(0o755)
