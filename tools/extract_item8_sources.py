"""Extract hash-bound packaged JSON with uv run -m tools.extract_item8_sources."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import packaged_sources, retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def provider_scope(root: Path) -> dict[str, JsonValue]:
    """Join every frozen provider to existing candidate evidence, without accepting families."""
    inputs = {
        "sources/packaged-json-redacted.json.gz":
            "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd",
        "sources/templates-redacted.json.gz":
            "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705",
        "sources/generation-code-references.json.gz":
            "95b9991457704f4cf710b09456a82db78c2dcdd79544212c77d8f31d64c8883f",
    }
    catalogs: list[dict[str, JsonValue]] = []
    sources = retained_sources(root)
    expected = [{"name": source.name, "sha256": source.sha256} for source in sources]
    for path, digest in inputs.items():
        raw = (root / "evidence/item-8" / path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            message = f"provider scope input changed: {path}"
            raise ValueError(message)
        catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
        if catalog["archives"] != expected:
            message = f"provider scope archive coverage mismatch: {path}"
            raise ValueError(message)
        catalogs.append(catalog)
    providers: list[JsonValue] = []
    for source in sources:
        selected = [
            [r for r in cast("list[dict[str, JsonValue]]", catalog["resources"])
             if str(r["archive"]).split("!/")[0] == source.name]
            for catalog in catalogs
        ]
        data, templates, code = selected
        resources: dict[str, JsonValue] = {}
        for kind in ("worldgen/structure", "worldgen/configured_feature",
                     "worldgen/template_pool", "lithostitched/worldgen_modifier",
                     "neoforge/biome_modifier"):
            resources[kind] = [
                {"archive": r["archive"], "path": r["path"]} for r in data
                if resource_identity(str(r["path"]), kind) is not None
            ]
        lane = "no_generation_candidates"
        if resources["worldgen/structure"]:
            lane = "packaged_structure_definitions"
        elif templates or any(resources.values()):
            lane = "other_packaged_generation_candidates"
        elif code:
            lane = "code_references_only"
        providers.append({
            "review_lane": lane,
            "archive": source.name, "sha256": source.sha256,
            "packaged_candidates": resources,
            "templates": [{"archive": r["archive"], "path": r["path"]} for r in templates],
            "code_candidates": [{"archive": r["archive"], "path": r["path"]} for r in code],
        })
    return {
        "scope": "Whole-stack candidate review inventory. Not semantic family acceptance.",
        "inputs": cast("JsonValue", inputs), "providers": providers,
    }


def main() -> None:
    """Write deterministic compressed source evidence without overwriting an attempt."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument(
        "--kind", choices=("json", "template", "metadata", "code", "scope"), default="json"
    )
    args = parser.parse_args()
    root = cast("Path", args.root)
    output = cast("Path", args.output)
    kind = cast("Literal['json', 'template', 'metadata', 'code', 'scope']", args.kind)
    result = (provider_scope(root) if kind == "scope"
              else packaged_sources(retained_sources(root), kind))
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(raw, mtime=0))


if __name__ == "__main__":
    main()
