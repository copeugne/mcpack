"""Check omission and identity boundaries of the baseline assembly join."""

# pyright: standard
# ruff: noqa: D103, INP001, S101, ANN001, ANN201
import gzip
import hashlib
import json

import pytest
import summarize


@pytest.fixture
def inspection(tmp_path, monkeypatch):
    directory = tmp_path / "evidence/item-13/start-inspection"
    directory.mkdir(parents=True)
    bounds = [[0, 0, 0, 1, 1, 1]]
    candidate = {
        "id": "one",
        "world": "world",
        "family_id": "family",
        "root": "root",
        "dimension": "dimension",
        "seed_role": "ordinary",
        "piece_bounds_sha256": hashlib.sha256(
            json.dumps(bounds, separators=(",", ":")).encode()
        ).hexdigest(),
    }
    raw = json.dumps(
        {"worlds": {"world": {"world_backup_sha256": "backup"}}, "candidates": [candidate]}
    ).encode()
    (directory.parent / "candidates.json").write_bytes(raw)
    result = {
        "world": "world",
        "candidate_sha256": hashlib.sha256(raw).hexdigest(),
        "world_backup_sha256": "backup",
        "starts": [
            {
                "id": "one",
                "status": "SAVED",
                "incomplete_chunks": [],
                "required_chunks": 1,
                "start_nbt": {"Children": [{"id": "piece", "BB": bounds[0]}]},
            }
        ],
    }
    monkeypatch.setattr(summarize, "ROOT", tmp_path)
    monkeypatch.setattr(summarize, "__file__", str(directory / "summarize.py"))

    def save() -> None:
        raw = gzip.compress(json.dumps(result).encode(), mtime=0)
        (directory / "world.json.gz").write_bytes(raw)
        (directory / "execution.txt").write_text(
            json.dumps(
                {
                    "sha256": hashlib.sha256(raw).hexdigest(),
                    "starts": len(result["starts"]),
                }
            )
            + "\n"
        )

    save()
    return directory, result, save


@pytest.mark.usefixtures("inspection")
def test_complete_case_is_retained(capsys):
    summarize.main()
    output = json.loads(capsys.readouterr().out)
    assert output["totals"]["starts"] == 1
    assert output["family_root_dimension_candidates"]["family|root|dimension"][0]["id"] == "one"


def test_changed_bytes_rejected(inspection):
    directory, _, _ = inspection
    with (directory / "world.json.gz").open("ab") as stream:
        stream.write(b"changed")
    with pytest.raises(ValueError, match="input identity mismatch"):
        summarize.main()


@pytest.mark.parametrize("duplicate", [False, True])
def test_missing_or_duplicate_candidate_rejected(inspection, duplicate):
    _, result, save = inspection
    result["starts"] = result["starts"] * 2 if duplicate else []
    save()
    with pytest.raises(ValueError, match="omits or duplicates"):
        summarize.main()


def test_changed_bounds_rejected(inspection):
    _, result, save = inspection
    result["starts"][0]["start_nbt"]["Children"][0]["BB"][0] = 1
    save()
    with pytest.raises(ValueError, match="bounds disagree"):
        summarize.main()


def test_versioned_component_uses_frozen_mapping():
    element = {
        "element_type": "moogs_structures:versioned_single_pool_element",
        "location": "mns:1_21_9/giant_skull",
        "locations": {"1.21-1.21.8": "mns:giant_skull", "1.21.9-1.21.11": "mns:1_21_9/giant_skull"},
    }
    assert summarize.named_components({"pool_element": element}) == {"mns:giant_skull"}
