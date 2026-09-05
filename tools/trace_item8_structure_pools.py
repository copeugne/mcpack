"""Trace frozen start pools with uv run -m tools.trace_item8_structure_pools."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from tools.build_item8_structure_inputs import (
    ORDER_INPUTS,
    REGISTRY_PATH,
    REGISTRY_SHA256,
    RUNTIME_LOG,
    SOURCE_PATH,
    SOURCE_SHA256,
)

from mcpack_evidence.item8_pool_links import add_pool_elements, pool_links, template_links
from mcpack_evidence.item8_pool_trace import trace_pool
from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_resource_selection import (
    mod_conditions_match,
    runtime_mod_ids,
    select_resources,
)
from mcpack_evidence.item8_templates import template_content

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
    RUNTIME_LOG: ORDER_INPUTS[RUNTIME_LOG],
    "evidence/item-8/sources/lithostitched-pool-additions-code/identities.json":
        "f3aecd612d8fdfe23649887ea70032cdc4fc5b0db00276ae3c0e718bdadf0a75",
    "evidence/item-8/sources/neoforge-condition-code/identities.json":
        "6dfe814d7ed7691ed4f80d460e14c7b274881ecbfee8eb29837edf51e237ba43",
    "evidence/item-8/sources/neoforge-registry-loading-code/identities.json":
        "1bcc020827e31e893e47baf01e173e915197bd755f5034fd18ef38c1d828b1be",
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
    additions, modifier_report = _pool_modifiers(resources, enabled, overlay)
    add_pool_elements(pool_edges, additions)
    template_edges = template_links(list(templates.values()))
    traces: dict[str, JsonValue] = {}
    unsupported: dict[str, JsonValue] = {}
    for identifier in read_registry(ROOT / REGISTRY_PATH):
        document = cast("dict[str, JsonValue]", structures[identifier]["document"])
        start_pool = document.get("start_pool")
        if isinstance(start_pool, str):
            result = trace_pool(
                start_pool, pool_edges, template_edges, document.get("pool_aliases", [])
            )
            result["pool_aliases"] = document.get("pool_aliases", [])
            traces[identifier] = result
        else:
            unsupported[identifier] = {
                "type": document.get("type"),
                "reason": "no direct start_pool; inspect custom generation path",
            }
    referenced_templates = {
        template
        for trace in traces.values()
        for template in cast("list[str]", cast("dict[str, JsonValue]", trace)["templates"])
    }
    contents: dict[str, JsonValue] = {}
    for identifier in sorted(referenced_templates):
        resource = templates[identifier]
        document = cast("dict[str, JsonValue]", resource["document"])
        contents[identifier] = {
            "source": {key: resource[key] for key in ("archive", "path", "sha256")},
            "template_size_xyz": document["size"],
            **template_content(document),
        }
    result: dict[str, JsonValue] = {
        "inputs": dict(INPUTS),
        "scope": "possible pool/template links only; not assembled placement or family counts",
        "structures": traces,
        "template_contents": contents,
        "untraced_structures": unsupported,
        "excluded_pools": excluded_pools,
        "excluded_templates": excluded_templates,
        "pool_modifiers": modifier_report,
    }
    payload = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(payload, mtime=0))
    print(
        f"Traced {len(traces)} structures; {len(unsupported)} require custom generation inspection"
    )


def _pool_modifiers(
    resources: list[JsonValue], enabled: list[str], overlay: bool
) -> tuple[list[JsonValue], dict[str, JsonValue]]:
    mods = runtime_mod_ids((ROOT / RUNTIME_LOG).read_text())
    selected, excluded = select_resources(
        resources, "lithostitched/worldgen_modifier",
        enabled_packs=enabled, lithostitched_overlay=overlay,
    )
    additions: list[JsonValue] = []
    dispositions: list[JsonValue] = []
    for identifier, resource in selected.items():
        document = cast("dict[str, JsonValue]", resource["document"])
        kind = document.get("type")
        status = "untraced modifier type"
        if kind == "lithostitched:add_template_pool_elements":
            if "predicate" in document or "neoforge:value" in document:
                message = f"unresolved additional pool modifier condition or wrapper: {identifier}"
                raise ValueError(message)
            if mod_conditions_match(document.get("neoforge:conditions", []), set(mods)):
                additions.append(resource)
                status = "included in potential pool reachability"
            else:
                status = "excluded by NeoForge mod conditions"
        dispositions.append({
            "id": identifier, "type": kind, "status": status,
            "conditions": document.get("neoforge:conditions", []),
            **{key: resource[key] for key in ("archive", "path", "sha256")},
        })
    return additions, {
        "runtime_mod_lines": cast("JsonValue", mods),
        "dispositions": dispositions,
        "excluded_resource_layers": excluded,
        "scope": "additive potential links only; other modifier types and runtime hooks untraced",
    }


def _resources(path: str) -> list[JsonValue]:
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress((ROOT / path).read_bytes())))
    return cast("list[JsonValue]", catalog["resources"])


if __name__ == "__main__":
    main()
