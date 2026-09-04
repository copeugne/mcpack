"""Trace frozen start pools with uv run -m tools.trace_item8_structure_pools."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from tools.build_item8_structure_inputs import (
    REGISTRY_PATH,
    REGISTRY_SHA256,
    SOURCE_PATH,
    SOURCE_SHA256,
)

from mcpack_evidence.item8_pool_links import pool_links, template_links
from mcpack_evidence.item8_pool_trace import trace_pool
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import select_resources

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = "evidence/item-8/sources/templates-redacted.json.gz"
CONTEXT = "evidence/item-8/runtime/registry-r1/world-context.json"
CONFIG = "evidence/item-6/frozen/config/lithostitched.json"
INPUTS = {
    SOURCE_PATH: SOURCE_SHA256,
    REGISTRY_PATH: REGISTRY_SHA256,
    TEMPLATES: "b4a2ed8ff0d16ff06c224119f623f248e75e9c8c838fbf2455bf37936c6d3705",
    CONTEXT: "0615a2dcdeb2120a467648df95f69aa9f1ef53e8989ae8c2191028d6f5c1aca2",
    CONFIG: "d8a63933ec4757186a594debea59dd35724a0a895fe601b324f96217c28312df",
}


def main() -> None:
    """Write potential relationships, explicitly retaining unsupported structure paths."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    for path, expected in INPUTS.items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            message = f"frozen trace input mismatch: {path}"
            raise ValueError(message)
    context = cast("dict[str, JsonValue]", json.loads((ROOT / CONTEXT).read_bytes()))
    packs = cast("dict[str, JsonValue]", context["DataPacks"])
    enabled = cast("list[str]", packs["Enabled"])
    # This exact hash-bound JSON-with-comments config enables the inspected condition.
    overlay = b'"breaks_seed_parity": true' in (ROOT / CONFIG).read_bytes()
    resources = _resources(SOURCE_PATH)
    structures, _ = select_resources(
        resources, "worldgen/structure", enabled_packs=enabled, lithostitched_overlay=overlay
    )
    pools, excluded_pools = select_resources(
        resources, "worldgen/template_pool", enabled_packs=enabled, lithostitched_overlay=overlay
    )
    templates, excluded_templates = select_resources(
        _resources(TEMPLATES),
        "structure",
        enabled_packs=enabled,
        lithostitched_overlay=overlay,
    )
    pool_edges = pool_links(list(pools.values()))
    template_edges = template_links(list(templates.values()))
    traces: dict[str, JsonValue] = {}
    unsupported: dict[str, JsonValue] = {}
    for identifier in read_registry(ROOT / REGISTRY_PATH):
        document = cast("dict[str, JsonValue]", structures[identifier]["document"])
        start_pool = document.get("start_pool")
        if isinstance(start_pool, str):
            result = trace_pool(start_pool, pool_edges, template_edges)
            result["pool_aliases"] = document.get("pool_aliases", [])
            traces[identifier] = result
        else:
            unsupported[identifier] = {
                "type": document.get("type"),
                "reason": "no direct start_pool; inspect custom generation path",
            }
    result: dict[str, JsonValue] = {
        "inputs": dict(INPUTS),
        "scope": "possible pool/template links only; not assembled placement or family counts",
        "structures": traces,
        "untraced_structures": unsupported,
        "excluded_pools": excluded_pools,
        "excluded_templates": excluded_templates,
    }
    payload = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(payload, mtime=0))
    print(
        f"Traced {len(traces)} structures; {len(unsupported)} require custom generation inspection"
    )


def _resources(path: str) -> list[JsonValue]:
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress((ROOT / path).read_bytes())))
    return cast("list[JsonValue]", catalog["resources"])


if __name__ == "__main__":
    main()
