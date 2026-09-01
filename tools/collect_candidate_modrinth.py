"""Resolve exact candidate filenames against primary Modrinth API records."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Final, cast, final

from pydantic import JsonValue, TypeAdapter

from mcpack_evidence.item3 import build_search_queries, find_exact_modrinth_file

if TYPE_CHECKING:
    import http.client

JsonObject = dict[str, JsonValue]
_JSON_ADAPTER: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)
_OVERRIDES_ADAPTER: Final[TypeAdapter[dict[str, list[str]]]] = TypeAdapter(dict[str, list[str]])
_MAX_DOWNLOAD_ATTEMPTS = 3


@dataclass(frozen=True)
class _Arguments:
    """Parsed collector paths and request pacing."""

    inventory: Path
    raw_dir: Path
    output: Path
    query_overrides: Path | None
    delay: float


def _arguments() -> _Arguments:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--inventory", type=Path, required=True)
    _ = parser.add_argument("--raw-dir", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--query-overrides", type=Path)
    _ = parser.add_argument("--delay", type=float, default=0.3)
    namespace = parser.parse_args()
    return _Arguments(
        inventory=cast("Path", namespace.inventory),
        raw_dir=cast("Path", namespace.raw_dir),
        output=cast("Path", namespace.output),
        query_overrides=cast("Path | None", namespace.query_overrides),
        delay=cast("float", namespace.delay),
    )


@final
class _ApiShapeError(ValueError):
    """A primary API response did not have the required JSON shape."""


@final
class _ApiCache:
    """Content-addressed primary-response cache with reproducible request receipts."""

    def __init__(self, root: Path, delay: float) -> None:
        self._root = root
        self._delay = delay
        self._receipts: dict[str, JsonObject] = {}
        root.mkdir(parents=True, exist_ok=True)

    def get(self, url: str) -> JsonValue:
        key = hashlib.sha256(url.encode()).hexdigest()
        body_path = self._root / f"{key}.json"
        if body_path.is_file():
            body = body_path.read_bytes()
            source = "cache"
        else:
            body = self._download(url)
            temporary = body_path.with_suffix(".partial")
            _ = temporary.write_bytes(body)
            _ = temporary.replace(body_path)
            source = "network"
            time.sleep(self._delay)
        self._receipts[url] = {
            "url": url,
            "body_path": body_path.as_posix(),
            "body_size_bytes": len(body),
            "body_sha256": hashlib.sha256(body).hexdigest(),
            "source": source,
        }
        return _JSON_ADAPTER.validate_json(body)

    def write_receipts(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": "item3-modrinth-request-index-v1",
            "written_at": datetime.now(UTC).isoformat(),
            "requests": [self._receipts[url] for url in sorted(self._receipts)],
        }
        _ = path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    @staticmethod
    def _download(url: str) -> bytes:
        request = urllib.request.Request(  # noqa: S310
            url,
            headers={"User-Agent": "mcpack-evidence/0.1 (github.com/copeugne/mcpack)"},
        )
        for attempt in range(_MAX_DOWNLOAD_ATTEMPTS):
            try:
                response = cast(
                    "http.client.HTTPResponse",
                    urllib.request.urlopen(request, timeout=60),  # noqa: S310
                )
                try:
                    return response.read()
                finally:
                    response.close()
            except (TimeoutError, urllib.error.URLError):
                if attempt == _MAX_DOWNLOAD_ATTEMPTS - 1:
                    raise
                retry_delay = 1.0 if attempt == 0 else 2.0
                time.sleep(retry_delay)
        raise AssertionError


def _as_objects(value: JsonValue) -> list[JsonObject]:
    if not isinstance(value, list):
        raise _ApiShapeError
    return [row for row in value if isinstance(row, dict)]


def _search(cache: _ApiCache, query: str) -> list[JsonObject]:
    parameters = urllib.parse.urlencode(
        {
            "query": query,
            "limit": "10",
            "facets": '[["project_type:mod"]]',
        }
    )
    response = cache.get(f"https://api.modrinth.com/v2/search?{parameters}")
    if not isinstance(response, dict):
        raise _ApiShapeError
    return _as_objects(response.get("hits"))


def _project_versions(cache: _ApiCache, project_id: str) -> list[JsonObject]:
    response = cache.get(f"https://api.modrinth.com/v2/project/{project_id}/version")
    return _as_objects(response)


def _resolve_candidate(
    cache: _ApiCache,
    candidate: str,
    overrides: dict[str, list[str]],
) -> JsonObject:
    checked_projects: set[str] = set()
    queries = tuple(
        dict.fromkeys((*overrides.get(candidate, []), *build_search_queries(candidate)))
    )
    for query in queries:
        for hit in _search(cache, query):
            project_id = hit.get("project_id")
            if not isinstance(project_id, str) or project_id in checked_projects:
                continue
            checked_projects.add(project_id)
            versions = _project_versions(cache, project_id)
            match = find_exact_modrinth_file(candidate, versions)
            if match is None:
                continue
            version = next(row for row in versions if row.get("id") == match.version_id)
            project = cache.get(f"https://api.modrinth.com/v2/project/{project_id}")
            if not isinstance(project, dict):
                raise _ApiShapeError
            files = version.get("files")
            if not isinstance(files, list):
                raise _ApiShapeError
            return {
                "candidate_filename": candidate,
                "resolved": True,
                "query": query,
                "project": project,
                "version": version,
                "file": files[match.file_index],
            }
    return {
        "candidate_filename": candidate,
        "resolved": False,
        "queries": [cast("JsonValue", value) for value in queries],
        "checked_project_ids": [cast("JsonValue", value) for value in sorted(checked_projects)],
    }


def main() -> int:
    """Collect resumable exact-file identity evidence for the candidate inventory."""
    arguments = _arguments()
    candidates = tuple(
        line.strip()
        for line in arguments.inventory.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    cache = _ApiCache(arguments.raw_dir / "responses", arguments.delay)
    overrides = (
        _OVERRIDES_ADAPTER.validate_json(arguments.query_overrides.read_bytes())
        if arguments.query_overrides is not None
        else {}
    )
    rows: list[JsonObject] = []
    for index, candidate in enumerate(candidates, start=1):
        row = _resolve_candidate(cache, candidate, overrides)
        rows.append(row)
        state = "resolved" if row["resolved"] else "unresolved"
        print(f"[{index:03d}/{len(candidates):03d}] {state}: {candidate}", flush=True)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "schema_version": "item3-modrinth-exact-discovery-v1",
        "retrieved_at": datetime.now(UTC).isoformat(),
        "inventory_count": len(candidates),
        "resolved_count": sum(row["resolved"] is True for row in rows),
        "rows": rows,
    }
    _ = arguments.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    cache.write_receipts(arguments.raw_dir / "request-index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
