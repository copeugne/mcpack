from __future__ import annotations

import hashlib
from io import BytesIO
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item7_restriction_inputs import ArchiveInput
from mcpack_evidence.item8_sources import packaged_json_sources

if TYPE_CHECKING:
    from pathlib import Path

    from pydantic import JsonValue


def zip_bytes(entries: dict[str, bytes]) -> bytes:
    stream = BytesIO()
    with ZipFile(stream, "w") as archive:
        for name, payload in entries.items():
            archive.writestr(name, payload)
    return stream.getvalue()


def source(tmp_path: Path, name: str, entries: dict[str, bytes]) -> ArchiveInput:
    payload = zip_bytes(entries)
    path = tmp_path / name
    _ = path.write_bytes(payload)
    return ArchiveInput(name, path, hashlib.sha256(payload).hexdigest())


def test_preserves_competing_optional_and_nested_resources(tmp_path: Path) -> None:
    path = "data/example/worldgen/structure/tower.json"
    first = source(tmp_path, "first.jar", {path: b'{"size":1}'})
    second = source(
        tmp_path,
        "second.jar",
        {
            path: b'{"size":2}',
            "packs/optional/" + path: b'{"size":3}',
            "META-INF/jarjar/library.jar": zip_bytes({path: b'{"size":4}'}),
        },
    )
    result = packaged_json_sources((first, second))
    rows = cast("list[dict[str, JsonValue]]", result["resources"])
    assert len(rows) == 4
    assert rows[0]["archive"] == "first.jar"
    assert rows[1]["archive"] == "second.jar!/META-INF/jarjar/library.jar"
    assert rows[3]["path"] == "packs/optional/" + path
    assert rows[0]["document"] == {"size": 1}
    assert rows[2]["document"] == {"size": 2}
    assert packaged_json_sources((first, second)) == result


def test_rejects_changed_archive(tmp_path: Path) -> None:
    item = source(tmp_path, "mod.jar", {})
    _ = item.path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="archive hash mismatch"):
        _ = packaged_json_sources((item,))


@pytest.mark.parametrize("name", ["../data/a/test.json", "/data/a/test.json"])
def test_rejects_escaped_members(tmp_path: Path, name: str) -> None:
    item = source(tmp_path, "mod.jar", {name: b"{}"})
    with pytest.raises(ValueError, match="unsafe ZIP member"):
        _ = packaged_json_sources((item,))


def test_comment_parsing_and_invalid_json_are_explicit(tmp_path: Path) -> None:
    path = "data/example/worldgen/structure/tower.json"
    item = source(tmp_path, "mod.jar", {path: b'// comment\n{"size":1}'})
    rows = cast("list[dict[str, JsonValue]]", packaged_json_sources((item,))["resources"])
    assert rows[0]["parser"] == "json-with-line-comments-removed"
    invalid = source(tmp_path, "bad.jar", {path: b"{invalid}"})
    failures = cast("list[dict[str, JsonValue]]", packaged_json_sources((invalid,))["resources"])
    assert failures[0]["parser"] == "invalid-json"
    assert failures[0]["document"] is None
    assert failures[0]["raw_text"] == "{invalid}"
    assert "cannot decode packaged JSON" in str(failures[0]["parse_error"])
