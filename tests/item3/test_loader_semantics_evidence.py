from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast

EVIDENCE_PATH = Path("evidence/item-3/loader-semantics-sources.json")
EXPECTED_COMMIT = "96010059ad23bfcef8be966c1a675a3abe4c8867"
EXPECTED_SOURCE_HASHES = {
    "BuiltInLanguageLoader.java": (
        "04b2e205ff98108c1d78bfea6b5c626d082c1d2426e084a4bcf4b98edf31aa17"
    ),
    "JarModsDotTomlModFileReader.java": (
        "34a924221e7158bbc3a8fdd9e204ec1d09a2996e7063bd8dd454a22633479016"
    ),
    "MavenVersionAdapter.java": "365131c98b70edee0e7b6dc2377c40e6ea56eff4d8127c842eeb687212f60c71",
    "ModInfo.java": "3b7af699f333f30ab5b24b7fb0316744365c4dff60e3d93036982c0867443585",
    "ModSorter.java": "a1aedb70f632305a9f360e1adb072aa818600df8442a327dba9ecc2785b12927",
    "VersionSupportMatrix.java": "a39dcd636dde637729376078fe156334c9424d38882c389defd633f65a1aaaf9",
}


def test_loader_semantics_receipt_is_complete_and_pinned() -> None:
    evidence = _evidence()
    fml_source = _dict(evidence["fml_source"])
    sources = _list_of_dicts(fml_source["files"])

    assert evidence["schema_version"] == "item3-loader-semantics-sources-v1"
    assert evidence["evidence_classification"] == "verified_primary_evidence"
    assert fml_source["commit"] == EXPECTED_COMMIT
    assert {_str(source["filename"]): _str(source["sha256"]) for source in sources} == (
        EXPECTED_SOURCE_HASHES
    )
    assert len(_list(evidence["verified_conclusions"])) == 7
    assert all(_str(value) for value in _list(evidence["limitations"]))


def test_loader_semantics_receipt_hashes_and_references_are_well_formed() -> None:
    evidence = _evidence()
    sources = _list_of_dicts(_dict(evidence["fml_source"])["files"])
    source_names = {_str(source["filename"]) for source in sources}

    for source in sources:
        digest = _str(source["sha256"])
        assert len(digest) == 64
        _ = bytes.fromhex(digest)
    target = _dict(evidence["target"])
    for artifact_name in ("fml_loader_artifact", "maven_artifact_runtime", "commons_lang_runtime"):
        digest = _str(_dict(target[artifact_name])["sha256"])
        assert hashlib.sha256(bytes.fromhex(digest)).digest_size == 32
    for conclusion in _list_of_dicts(evidence["verified_conclusions"]):
        assert {_str(value) for value in _list(conclusion["source_files"])} <= source_names


def _evidence() -> dict[str, object]:
    return _dict(cast("object", json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))))


def _dict(value: object) -> dict[str, object]:
    assert isinstance(value, dict)
    return cast("dict[str, object]", value)


def _list(value: object) -> list[object]:
    assert isinstance(value, list)
    return cast("list[object]", value)


def _list_of_dicts(value: object) -> list[dict[str, object]]:
    return [_dict(item) for item in _list(value)]


def _str(value: object) -> str:
    assert isinstance(value, str)
    return value
