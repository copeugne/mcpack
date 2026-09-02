from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import cast

EVIDENCE = Path("evidence/item-4/runtime-validation.json")


def test_all_seed_controls_pass_full_retained_lifecycle() -> None:
    evidence = _dict(cast("object", json.loads(EVIDENCE.read_text(encoding="utf-8"))))
    controls = [_dict(row) for row in _list(evidence["seed_controls"])]

    assert evidence["gate_status"] == "pass"
    assert {_str(row["role"]) for row in controls} == {
        "ordinary",
        "mountainous",
        "ocean-heavy",
        "biome-diverse",
    }
    assert all(row["materialized"] is True for row in controls)
    assert all(row["initial_boot_validated"] is True for row in controls)
    assert all(row.get("clean_stop", True) is True for row in controls)
    for row in controls:
        observation = _dict(row["world_seed_observation"])
        assert observation["nbt_path"] == "Data.WorldGenSettings.seed"
        assert observation["observed_seed"] == row["seed"]


def test_committed_lifecycle_logs_match_hashes_and_events() -> None:
    evidence = _dict(cast("object", json.loads(EVIDENCE.read_text(encoding="utf-8"))))
    controls = [_dict(row) for row in _list(evidence["seed_controls"])]
    log_rows = [row for row in controls if "log" in row]
    log_rows.append(_dict(evidence["ordinary_initial_boot"]))
    log_rows.append(_dict(evidence["restore_boot"]))

    for row in log_rows:
        path = Path(_str(row["log"]))
        assert path.stat().st_size == row["log_size_bytes"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["log_sha256"]
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            log = stream.read()
        assert "Done (" in log
        assert "Saved the game" in log
        assert "Stopping server" in log


def test_backup_and_restore_receipts_agree() -> None:
    evidence = _dict(cast("object", json.loads(EVIDENCE.read_text(encoding="utf-8"))))
    backup = _dict(
        cast(
            "object",
            json.loads(Path("evidence/item-4/ordinary-backup-receipt.json").read_text()),
        )
    )
    restore = _dict(
        cast(
            "object",
            json.loads(Path("evidence/item-4/ordinary-restore-receipt.json").read_text()),
        )
    )
    summary = _dict(evidence["backup"])

    assert backup["archive_sha256"] == summary["archive_sha256"]
    assert restore["archive_sha256"] == backup["archive_sha256"]
    assert restore["world_file_count"] == backup["world_file_count"] == 57
    files = [_dict(row) for row in _list(backup["world_files"])]
    assert "session.lock" not in {_str(row["path"]) for row in files}
    assert summary["session_lock_excluded"] is True


def _dict(value: object) -> dict[str, object]:
    assert isinstance(value, dict)
    return cast("dict[str, object]", value)


def _list(value: object) -> list[object]:
    assert isinstance(value, list)
    return cast("list[object]", value)


def _str(value: object) -> str:
    assert isinstance(value, str)
    return value
