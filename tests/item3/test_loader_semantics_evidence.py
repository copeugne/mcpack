from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict, cast


class _Source(TypedDict):
    path: str
    url: str
    sha256: str


class _Conclusion(TypedDict):
    source_paths: list[str]


class _Loader(TypedDict):
    commit: str
    sources: list[_Source]


class _Target(TypedDict):
    minecraft: str
    neoforge: str
    fml_implementation_version: str


class _Receipt(TypedDict):
    schema_version: str
    target: _Target
    fancy_mod_loader: _Loader
    conclusions: list[_Conclusion]


def test_loader_semantics_receipt_has_exact_sources() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    receipt_path = repo_root / "evidence/item-3/loader-semantics-sources.json"
    receipt = cast("_Receipt", json.loads(receipt_path.read_text(encoding="utf-8")))

    assert receipt["schema_version"] == "item3-loader-semantics-sources-v1"
    assert receipt["target"]["minecraft"] == "1.21.1"
    assert receipt["target"]["neoforge"] == "21.1.249"
    assert receipt["target"]["fml_implementation_version"] == "4.0"
    assert receipt["fancy_mod_loader"]["commit"] == "96010059ad23bfcef8be966c1a675a3abe4c8867"
    sources = receipt["fancy_mod_loader"]["sources"]
    assert len(sources) == 6
    assert len({source["path"] for source in sources}) == 6
    assert all(len(source["sha256"]) == 64 for source in sources)
    commit = receipt["fancy_mod_loader"]["commit"]
    raw_prefix = f"https://raw.githubusercontent.com/neoforged/FancyModLoader/{commit}/"
    assert all(source["url"].startswith(raw_prefix) for source in sources)
    source_paths = {source["path"] for source in sources}
    assert all(
        set(conclusion["source_paths"]).issubset(source_paths)
        for conclusion in receipt["conclusions"]
    )
