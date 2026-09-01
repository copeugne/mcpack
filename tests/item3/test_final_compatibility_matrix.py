from __future__ import annotations

import json
from pathlib import Path
from typing import cast

MATRIX = Path("evidence/item-3/final-compatibility-matrix.json")
RETAINED = Path("evidence/item-3/runtime/retained-server-candidates.txt")


def test_final_matrix_covers_inventory_once_and_has_no_unresolved_disposition() -> None:
    matrix = _dict(cast("object", json.loads(MATRIX.read_text(encoding="utf-8"))))
    rows = [_dict(value) for value in _list(matrix["rows"])]
    filenames = [_str(row["candidate_filename"]) for row in rows]

    assert matrix["schema_version"] == "item3-final-compatibility-matrix-v1"
    assert matrix["candidate_count"] == 190
    assert len(filenames) == len(set(filenames)) == 190
    assert all(not _str(row["final_disposition"]).startswith("unresolved") for row in rows)


def test_retained_rows_match_runtime_manifest_and_pass_static_gates() -> None:
    matrix = _dict(cast("object", json.loads(MATRIX.read_text(encoding="utf-8"))))
    rows = [_dict(value) for value in _list(matrix["rows"])]
    retained_rows = [row for row in rows if row["final_disposition"] == "retained_server"]
    retained_manifest = set(RETAINED.read_text(encoding="utf-8").splitlines())

    assert {_str(row["candidate_filename"]) for row in retained_rows} == retained_manifest
    assert len(retained_rows) == 136
    assert all(row["static_status"] == "compatible" for row in retained_rows)
    assert all(
        _dict(row["publisher_environment"])["server"] != "unsupported" for row in retained_rows
    )
    assert all(row["runtime_evidence"] is not None for row in retained_rows)
    assert all(
        {_str(value) for value in _list(check["provider_candidates"])}.issubset(retained_manifest)
        for row in retained_rows
        for check in (_dict(value) for value in _list(row["dependency_checks"]))
    )


def _dict(value: object) -> dict[str, object]:
    assert isinstance(value, dict)
    return cast("dict[str, object]", value)


def _list(value: object) -> list[object]:
    assert isinstance(value, list)
    return cast("list[object]", value)


def _str(value: object) -> str:
    assert isinstance(value, str)
    return value
