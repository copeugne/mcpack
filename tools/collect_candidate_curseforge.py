"""Collect exact candidate records from CurseForge's official website API."""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import urllib.parse
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar, cast

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class _FileLocator(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    project_id: int = Field(gt=0)
    file_id: int = Field(gt=0)


class _FileRecord(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    id: int
    file_name: str = Field(alias="fileName")
    display_name: str = Field(alias="displayName")
    file_length: int = Field(ge=0, alias="fileLength")
    game_versions: tuple[str, ...] = Field(alias="gameVersions")
    release_type: int = Field(alias="releaseType")
    date_created: str = Field(alias="dateCreated")
    date_modified: str = Field(alias="dateModified")


class _Response(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    data: _FileRecord


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    file_map: Path
    raw_dir: Path
    output: Path


_MAP_ADAPTER = TypeAdapter(dict[str, _FileLocator])
_HTTP_OK = 200


def _arguments() -> _Arguments:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--file-map", type=Path, required=True)
    _ = parser.add_argument("--raw-dir", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    namespace = parser.parse_args()
    return _Arguments(
        file_map=cast("Path", namespace.file_map),
        raw_dir=cast("Path", namespace.raw_dir),
        output=cast("Path", namespace.output),
    )


def _cdn_url(file_id: int, filename: str) -> str:
    digits = str(file_id)
    return f"https://edge.forgecdn.net/files/{digits[:-3]}/{digits[-3:]}/{filename}"


def _acquire(url: str, path: Path) -> bytes:
    if not path.is_file():
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme != "https" or parsed.hostname != "www.curseforge.com":
            raise ValueError
        connection = http.client.HTTPSConnection(parsed.hostname, timeout=60)
        request_target = parsed.path
        if parsed.query:
            request_target = f"{request_target}?{parsed.query}"
        connection.request("GET", request_target)
        response = connection.getresponse()
        if response.status != _HTTP_OK:
            connection.close()
            raise ConnectionError(response.status)
        body = response.read()
        connection.close()
        temporary = path.with_suffix(".partial")
        _ = temporary.write_bytes(body)
        _ = temporary.replace(path)
    return path.read_bytes()


def main() -> int:
    """Verify every mapped exact CurseForge file and preserve its raw response."""
    arguments = _arguments()
    file_map = _MAP_ADAPTER.validate_json(arguments.file_map.read_bytes())
    arguments.raw_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    requests: list[dict[str, object]] = []
    for candidate, locator in file_map.items():
        source_url = (
            f"https://www.curseforge.com/api/v1/mods/{locator.project_id}/files/{locator.file_id}"
        )
        response_path = arguments.raw_dir / f"{locator.project_id}-{locator.file_id}.json"
        body = _acquire(source_url, response_path)
        response = _Response.model_validate_json(body)
        if response.data.id != locator.file_id or response.data.file_name != candidate:
            raise ValueError
        rows.append(
            {
                "candidate_filename": candidate,
                "project_id": locator.project_id,
                "file_id": locator.file_id,
                "source_url": source_url,
                "cdn_url": _cdn_url(locator.file_id, candidate),
                "record": response.data.model_dump(mode="json", by_alias=True),
            }
        )
        requests.append(
            {
                "url": source_url,
                "body_path": response_path.as_posix(),
                "body_size_bytes": len(body),
                "body_sha256": hashlib.sha256(body).hexdigest(),
            }
        )
        print(f"verified: {candidate}", flush=True)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "schema_version": "item3-curseforge-exact-discovery-v1",
        "retrieved_at": datetime.now(UTC).isoformat(),
        "resolved_count": len(rows),
        "rows": rows,
    }
    _ = arguments.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    index = {
        "schema_version": "item3-curseforge-request-index-v1",
        "written_at": datetime.now(UTC).isoformat(),
        "requests": requests,
    }
    _ = (arguments.raw_dir / "request-index.json").write_text(
        json.dumps(index, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
