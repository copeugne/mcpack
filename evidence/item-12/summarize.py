"""Build the Item 12 result report from retained, identity-bound observations."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, INP001, E501
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from tools.analyze_discoverability import FIELDS, PROTOCOL
from tools.analyze_route_opportunities import ROOT, accepted_inputs, read_bound

from mcpack_evidence.item7_archive_models import ArchiveManifest


def counts(rays: list[dict[str, Any]]) -> str:
    c = Counter(r["status"] for r in rays)
    return f"{c['CLEAR']}/{c['OCCLUDED']}/{c['UNKNOWN']} of {len(rays)}"


def build(results: Path, *, representative: bool = False) -> str:
    names = ["full-ordinary-r1-baseline"] if representative else sorted(accepted_inputs())
    actual = {p.name.removesuffix(".json.gz") for p in results.glob("*.json.gz")}
    if not representative and actual != set(names):
        raise ValueError("incomplete or extra result matrix")
    docs = []
    for name in names:
        raw = read_bound(results / f"{name}.json.gz")
        digest = hashlib.sha256(raw).hexdigest()
        log = read_bound(ROOT / "evidence/item-12/validation/full" / f"{name}.txt").decode()
        producer = json.loads(next(line for line in log.splitlines() if line.startswith("{")))
        if (
            producer["sha256"] != digest
            or producer["world"] != name
            or producer["bytes"] != len(raw)
        ):
            raise ValueError("result differs from retained producer output")
        doc = json.loads(gzip.decompress(raw))
        manifest_raw = read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
        manifest = ArchiveManifest.model_validate_json(manifest_raw)
        expected = {
            "census_sha256": accepted_inputs()[name]["input_sha256"],
            "archive_manifest_sha256": hashlib.sha256(manifest_raw).hexdigest(),
            "world_backup_sha256": next(
                r.sha256 for r in manifest.files if r.relative_path == "world-backup.json"
            ),
            "protocol_sha256": hashlib.sha256(read_bound(PROTOCOL)).hexdigest(),
            "producer_sha256": hashlib.sha256(
                read_bound(ROOT / "tools/analyze_discoverability.py")
            ).hexdigest(),
            "shared_reader_sha256": hashlib.sha256(
                read_bound(ROOT / "tools/analyze_route_opportunities.py")
            ).hexdigest(),
        }
        if (
            doc["inputs"] != expected
            or doc["world"] != name
            or doc["protocol"] != "item12-discoverability-v1"
        ):
            raise ValueError("result provenance mismatch")
        if len(doc["cases"]) != producer["cases"]:
            raise ValueError("case denominator differs from producer")
        docs.append((doc, digest))
    lines = [
        "# Item 12 discoverability results",
        "",
        "Representative only. Full Item 12 gate remains open."
        if representative
        else "Complete predeclared viewpoint matrix. See README for acceptance, review and delivery status.",
        "",
        "Protocol: [item12-discoverability-v1](protocol.md). Human recognition and player discovery rates: NOT MEASURED.",
        "",
        "These are family-balanced saved-world cases, not discovery probabilities. Each case retains its full family abundance per 4,096 chunks separately from geometric rays. Overworld only; other dimensions retain Item 8 source assessment and Item 10 density. Architectural/entrance judgments are in [assessments](assessments.md); navigation evidence is [separate](navigation-source/README.md).",
        "",
        "C/O/U means CLEAR/OCCLUDED/UNKNOWN, followed by the full ray denominator. Low/high use the complete eight-cell ring; UNKNOWN means at least one missing eye. Relief can include buildings or water, not just terrain. A clear envelope point is not a visible authored block, recognizable silhouette or entrance.",
        "",
        "WORLD_SURFACE (WS) and MOTION_BLOCKING_NO_LEAVES (NL) use the same observer eye. NL is a foliage-sensitive heightmap comparison, not a measured no-trees world. Finite boundaries, fluid opacity, ignored overhangs/caves, purposive seeds and two repetitions limit interpretation. Zeroes do not prove absence.",
        "",
    ]
    for doc, digest in docs:
        name = doc["world"]
        lines += [
            f"## {name}",
            "",
            f"[Raw observations](results/{name}.json.gz), SHA-256 `{digest}`. Selected cases: {len(doc['cases'])}.",
            "",
            "| Family and selected variant/location | Existing count / chunks | Recorded biome | Ring relief, blocks | Low WS; NL C/O/U | High WS; NL C/O/U | All eight WS; NL C/O/U |",
            "| --- | ---: | --- | ---: | --- | --- | --- |",
        ]
        for case in doc["cases"]:
            obs = case["observation"]

            def view(which: str, observation: dict[str, Any] = obs) -> str:
                index = observation.get(which)
                return (
                    "UNKNOWN extremum"
                    if index is None
                    else "; ".join(
                        counts(observation["views"][index]["rays"][field]) for field in FIELDS
                    )
                )

            all_views = "; ".join(
                counts([ray for v in obs["views"] for ray in v["rays"][field]]) for field in FIELDS
            )
            lines.append(
                f"| {case['family_id']}<br>{case['location_id']} | {case['family_count']} / {case['density_chunks']} | {case['biome'] or 'UNKNOWN'} | {obs.get('relief')} | {view('low_view')} | {view('high_view')} | {all_views} |"
            )
        lines += [
            "",
            "### Biome-grouped ray denominators",
            "",
            "Group by accepted target-biome attribution, not observer biome. Each family contributes one case; common-family occurrence counts do not weight these rays.",
            "",
            "| Biome | Cases | WS C/O/U | NL C/O/U | WS occluded, NL clear / paired rays |",
            "| --- | ---: | --- | --- | --- |",
        ]
        for biome in sorted({str(c["biome"]) for c in doc["cases"]}):
            cases = [c for c in doc["cases"] if str(c["biome"]) == biome]
            ws = [r for c in cases for v in c["observation"]["views"] for r in v["rays"][FIELDS[0]]]
            nl = [r for c in cases for v in c["observation"]["views"] for r in v["rays"][FIELDS[1]]]
            contrast = sum(
                a["status"] == "OCCLUDED" and b["status"] == "CLEAR"
                for a, b in zip(ws, nl, strict=True)
            )
            lines.append(
                f"| {biome} | {len(cases)} | {counts(ws)} | {counts(nl)} | {contrast} / {len(ws)} |"
            )
        lines += [""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--representative", action="store_true")
    args = parser.parse_args()
    text = build(args.results, representative=args.representative)
    with args.output.open("x") as stream:
        stream.write(text)


if __name__ == "__main__":
    main()
