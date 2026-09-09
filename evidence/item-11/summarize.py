"""Rebuild the complete Item 11 report from the fixed accepted result matrix."""

# pyright: standard
# ruff: noqa: D103, EM101, TRY003, PLR2004, INP001
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any, cast

from tools.analyze_route_opportunities import (
    RADII,
    ROOT,
    ROUTES,
    SPEEDS,
    WINDOWS,
    accepted_inputs,
    category_occurrences,
    distribution,
    read_bound,
)

from mcpack_evidence.item6_json import parse_strict_json
from mcpack_evidence.item7_archive_models import ArchiveManifest

CATEGORIES = (
    "all_locations",
    "actionable_candidates",
    "encounter_sites",
    "T2",
    "T3",
    "T4",
    "villages",
)


def primary(route: dict[str, Any], category: str = "all_locations") -> dict[str, Any]:
    return next(
        row
        for row in route["summaries"]
        if row["radius"] == 64 and row["window"] == 768 and row["category"] == category
    )


def cost_text(value: dict[str, float] | None) -> str:
    if value is None:
        return "null"
    return (
        f"{value['central_seconds']:.2f} [{value['min_seconds']:.2f}, {value['max_seconds']:.2f}]"
    )


def repeat_text(values: list[dict[str, float]], window: int) -> str:
    if not values:
        return f"0; No repeat: right-censored at {window} blocks"
    central = distribution([v["central_seconds"] for v in values])
    low = min(v["min_seconds"] for v in values)
    high = max(v["max_seconds"] for v in values)
    return (
        f"{len(values)}; median {central['median']:.2f}; IQR {central['iqr']:.2f}; "
        f"central [{central['min']:.2f}, {central['max']:.2f}]; speed [{low:.2f}, {high:.2f}]"
    )


def distribution_text(value: dict[str, Any]) -> str:
    if not value["n"]:
        return "0; NA"
    return (
        f"{value['n']}; {value['median']:.2f}; {value['iqr']:.2f}; "
        f"[{value['min']:.2f}, {value['max']:.2f}]"
    )


def build(directory: Path) -> str:  # noqa: C901, PLR0912, PLR0915 - one fixed report, no new framework
    worlds = {}
    hashes = {}
    expected_categories = set(category_occurrences([], total_name="all_locations"))
    code_hash = hashlib.sha256(
        read_bound(ROOT / "tools/analyze_route_opportunities.py")
    ).hexdigest()
    protocol_hash = hashlib.sha256(read_bound(ROOT / "evidence/item-11/protocol.md")).hexdigest()
    accepted = accepted_inputs()
    if len(accepted) != 16:
        raise ValueError("accepted source matrix must contain sixteen worlds")
    for name, source in accepted.items():
        raw = read_bound(directory / (name + ".json.gz"))
        # Reuse the producer's retained stdout identity, not self-asserted input hashes.
        log = read_bound(ROOT / "evidence/item-11/validation/full" / (name + ".txt"))
        produced = cast("dict[str, Any]", parse_strict_json(log.splitlines()[0]))
        if (produced["world"], produced["output_bytes"], produced["sha256"]) != (
            name,
            len(raw),
            hashlib.sha256(raw).hexdigest(),
        ):
            raise ValueError("result digest differs from retained producer output")
        result = cast("dict[str, Any]", parse_strict_json(gzip.decompress(raw)))
        if result["world"] != name or result["protocol"] != "item11-routes-v2":
            raise ValueError("route result world/protocol mismatch")
        if result["inputs"]["census_sha256"] != source["input_sha256"]:
            raise ValueError("route result does not bind the accepted census")
        manifest_raw = read_bound(ROOT / "evidence/item-10" / name / "archive-manifest.json")
        manifest = ArchiveManifest.model_validate_json(manifest_raw)
        backup = next(r for r in manifest.files if r.relative_path == "world-backup.json")
        if (
            result["inputs"]["archive_manifest_sha256"] != hashlib.sha256(manifest_raw).hexdigest()
            or result["inputs"]["world_backup_sha256"] != backup.sha256
        ):
            raise ValueError("route result world provenance mismatch")
        if (
            result["inputs"]["analysis_sha256"] != code_hash
            or result["inputs"]["protocol_sha256"] != protocol_hash
        ):
            raise ValueError("route result does not bind current code and protocol")
        if set(result["routes"]) != set(ROUTES) or result["human_metrics"] != "NOT MEASURED":
            raise ValueError("incomplete route matrix or mislabeled human metrics")
        for route in result["routes"].values():
            keys = [(r["radius"], r["window"], r["category"]) for r in route["summaries"]]
            expected = {
                (radius, window, category)
                for radius in RADII
                for window in WINDOWS
                for category in expected_categories
            }
            if (
                len(keys) != len(expected)
                or set(keys) != expected
                or set(route["transport"]) != set(SPEEDS)
            ):
                raise ValueError("incomplete window/radius/category/mode matrix")
            # Keep the report view small; raw observations remain in the checked input file.
            del route["observations"]
            for model in route["transport"].values():
                model["failure_reasons"] = sorted(
                    {reason for failure in model["failures"] for reason in failure["reasons"]}
                )
                del model["failures"], model["cumulative_cost_distance"]
            for row in route["summaries"]:
                for values in row["modes"].values():
                    values["adjacent_time"] = repeat_text(
                        values.pop("unconstrained_adjacent_repeat_interval_times"), row["window"]
                    )
                    values["visible_time"] = repeat_text(
                        values.pop("unconstrained_repeat_interval_times"), row["window"]
                    )
                for population in ("adjacent", "geometric_visible"):
                    for key in ("events", "gaps", "repeats"):
                        del row[population][key]
        del result["top_cells"]
        worlds[name] = result
        hashes[name] = hashlib.sha256(raw).hexdigest()
    lines = [
        "# Item 11 complete automated route measurements",
        "",
        "Local matrix: PASS. Review and main delivery are separate gates recorded in README.md.",
        "",
        "Sixteen accepted saved worlds, 64 fixed Overworld transects and 192 route/mode evaluations.",  # noqa: E501 - generated Markdown row
        "Each route is 768 blocks. Primary adjacency radius is 64 blocks. Coverage is sampled",
        "eight-block segments with a ray-clear proxy target, not observed human discovery.",
        "Route membership totals below can count a location on several overlapping transects.",
        "C/T1/T2/T3/T4 roles are provisional, retaining confidence and ambiguity in each raw row.",
        "",
        "## Per-world primary candidate membership",
        "",
        "| World | All | Actionable | Encounter sites | T2 | T3 | T4 | Village | Ray-clear all | Covered blocks / 3072 |",  # noqa: E501 - generated Markdown row
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, world in worlds.items():
        counts = [
            sum(primary(r, c)["adjacent"]["count"] for r in world["routes"].values())
            for c in CATEGORIES
        ]
        visible = sum(primary(r)["geometric_visible"]["count"] for r in world["routes"].values())
        covered = sum(primary(r)["covered_blocks"] for r in world["routes"].values())
        lines.append(
            "| "
            + name.removeprefix("full-")
            + " | "
            + " | ".join(map(str, [*counts, visible, covered]))
            + " |"
        )
    lines += [
        "",
        "## Per-route primary category membership and coverage",
        "",
        "Each cell is adjacent count / ray-clear count / covered blocks / UNKNOWN-only blocks.",
        "Radius is 64 blocks and every coverage denominator is 768 sampled route blocks.",
        "UNKNOWN-only blocks have an UNKNOWN ray but no ray-clear target at the sampled station.",
        "UNKNOWN-only numerators are reported even when zero.",
        "Categories overlap; adjacent and visible populations are independently selected.",
        "Zeroes are retained. These are geometric proxies, not human encounters or activities.",
        "",
        "| World / route | All | Actionable | Encounter sites | T2 | T3 | T4 | Village |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for name, world in worlds.items():
        for label, route in world["routes"].items():
            cells = [
                f"{row['adjacent']['count']} / {row['geometric_visible']['count']} / {row['covered_blocks']} / {row['unknown_only_blocks']}"  # noqa: E501 - generated Markdown cell
                for row in (primary(route, category) for category in CATEGORIES)
            ]
            lines.append(f"| {name.removeprefix('full-')} / {label} | {' | '.join(cells)} |")
    lines += [
        "",
        "## Per-route primary gaps, repetition and transport",
        "",
        "All-location gaps include censored beginning/end intervals. First repeat is distance from",
        "route start; NR means no repeat, right-censored at 768. Prefixes are walking/horse/boat",
        "model-reachable blocks. F denotes MODEL_FEASIBLE, I INFEASIBLE, U UNKNOWN.",
        "Raw rows retain every failure station, cost range and category-specific interval.",
        "",
        "| World / route | Adjacent | Ray-clear | Maximum empty gap | First repeat | Prefixes | Mode status |",  # noqa: E501 - generated Markdown row
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for name, world in worlds.items():
        for label, route in world["routes"].items():
            row = primary(route)
            prefixes = "/".join(str(route["transport"][m]["reachable_prefix"]) for m in SPEEDS)
            status = "/".join(
                {"MODEL_FEASIBLE": "F", "INFEASIBLE": "I", "UNKNOWN": "U"}[
                    route["transport"][m]["status"]
                ]
                for m in SPEEDS
            )
            repeat = row["adjacent"]["first_repeat_distance"]
            lines.append(
                f"| {name.removeprefix('full-')} / {label} | {row['adjacent']['count']} | {row['geometric_visible']['count']} | {row['adjacent']['maximum_empty_interval']} | {repeat if repeat is not None else 'NR'} | {prefixes} | {status} |"  # noqa: E501 - generated Markdown row
            )
    lines += [
        "",
        "## Modeled travel costs",
        "",
        "Primary 64-block radius, full 768-block window, all-location group; all 192 mode rows.",
        "Values are central seconds [fast-speed seconds, slow-speed seconds], rounded to two decimals.",  # noqa: E501 - report prose
        "Completed costs are null for INFEASIBLE/UNKNOWN full-route modes. Prefix costs stop at",
        "the retained reachable prefix; unconstrained costs ignore feasibility and are not actual travel.",  # noqa: E501 - report prose
        "Failure reasons list distinct retained codes across all stations for that route/mode.",
        "NO_DRY_SUPPORT means a wet/air surface; NO_LEVEL_3X3_WATER means the boat corridor",
        "lacks level water width. HEIGHT_STEP_EXCEEDS_CAPABILITY is an excessive height change.",
        "UNKNOWN_TOP_BLOCK and UNKNOWN_WATER_NEIGHBORHOOD mean unavailable block evidence.",
        "None means the model has no recorded failure. Exact failure stations remain in raw results.",  # noqa: E501 - report prose
        "Complete window/category costs are reported with reachable coverage below; raw values are unrounded.",  # noqa: E501 - report prose
        "",
        "| World / route / mode | Completed seconds | Prefix seconds | Unconstrained seconds | Failure reasons |",  # noqa: E501 - generated Markdown row
        "| --- | --- | --- | --- | --- |",
    ]
    for name, world in worlds.items():
        for label, route in world["routes"].items():
            for mode, costs in primary(route)["modes"].items():
                reasons = ", ".join(route["transport"][mode]["failure_reasons"]) or "None"
                lines.append(
                    f"| {name.removeprefix('full-')} / {label} / {mode} | {cost_text(costs['completed_cost'])} | {cost_text(costs['prefix_cost'])} | {cost_text(costs['unconstrained_cost'])} | {reasons} |"  # noqa: E501 - generated Markdown row
                )
    lines += [
        "",
        "## Modeled repeated-family interval times",
        "",
        "Same primary group/window and all 192 modes. Adjacent-anchor and first-ray-clear events",
        "remain separate. Each cell gives interval count, central-speed median and IQR, central-speed",  # noqa: E501 - report prose
        "minimum/maximum, and the envelope across all intervals and the declared speed range.",
        "All times are unconstrained modeled seconds, including for infeasible modes. The speed",
        "envelope expresses assumptions plus interval spread, not a population confidence interval.",  # noqa: E501 - report prose
        "Zero ties are retained. No-repeat rows are right-censored at 768 blocks, not infinite variety.",  # noqa: E501 - report prose
        "All category/window/radius time summaries appear with distance statistics below.",
        "",
        "| World / route / mode | Adjacent-family interval seconds | Ray-clear-family interval seconds |",  # noqa: E501 - generated Markdown row
        "| --- | --- | --- |",
    ]
    for name, world in worlds.items():
        for label, route in world["routes"].items():
            for mode, costs in primary(route)["modes"].items():
                lines.append(
                    f"| {name.removeprefix('full-')} / {label} / {mode} | {costs['adjacent_time']} | {costs['visible_time']} |"  # noqa: E501 - generated Markdown row
                )
    lines += [
        "",
        "## Radius and distance sensitivity",
        "",
        "Each row pools 32 routes within one arm. These are overlapping fixed transects, not",
        "independent samples. Coverage denominator is 32 times the window length.",
        "",
        "| Arm | Radius | Window | Adjacent memberships | Ray-clear memberships | Covered / denominator | Unknown-only / denominator |",  # noqa: E501 - generated Markdown row
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for arm in ("baseline", "without-sparse"):
        selected = [
            w for n, w in worlds.items() if ("without-sparse" in n) == (arm == "without-sparse")
        ]
        for radius in RADII:
            for window in WINDOWS:
                rows = [
                    s
                    for w in selected
                    for r in w["routes"].values()
                    for s in r["summaries"]
                    if s["category"] == "all_locations"
                    and s["radius"] == radius
                    and s["window"] == window
                ]
                lines.append(
                    f"| {arm} | {radius} | {window} | {sum(s['adjacent']['count'] for s in rows)} | {sum(s['geometric_visible']['count'] for s in rows)} | {sum(s['covered_blocks'] for s in rows)} / {32 * window} | {sum(s['unknown_only_blocks'] for s in rows)} / {32 * window} |"  # noqa: E501 - generated Markdown row
                )
    lines += [
        "",
        "## Descriptive dispersion and paired contrasts",
        "",
        "JSON summaries below give n, median, minimum, maximum and inclusive IQR. No bootstrap",
        "population intervals are justified for these nonrandom seeds and overlapping routes.",
        "",
        "```json",
    ]
    stats = {}
    for arm in ("baseline", "without-sparse"):
        rows = [
            primary(r)
            for n, w in worlds.items()
            if ("without-sparse" in n) == (arm == "without-sparse")
            for r in w["routes"].values()
        ]
        stats[arm] = {
            "coverage_blocks": distribution([r["covered_blocks"] for r in rows]),
            "adjacent_count": distribution([r["adjacent"]["count"] for r in rows]),
            "maximum_empty_gap": distribution(
                [r["adjacent"]["maximum_empty_interval"] for r in rows]
            ),
            "first_repeat_distance_uncensored": distribution(
                [
                    r["adjacent"]["first_repeat_distance"]
                    for r in rows
                    if r["adjacent"]["first_repeat_distance"] is not None
                ]
            ),
        }
    lines += [
        json.dumps(stats, sort_keys=True, indent=2),
        "```",
        "",
        "Pair differences below are omit-Sparse minus baseline for the same seed/repetition.",
        "The final ocean-heavy r2 control uses the accepted third attempt. Rejected attempts",
        "remain in Item 10 custody and are not additional route samples.",
        "",
        "| Seed / repetition | Adjacent membership difference | Ray-clear membership difference | Covered-block difference |",  # noqa: E501 - generated Markdown row
        "| --- | ---: | ---: | ---: |",
    ]
    for name, baseline in worlds.items():
        if not name.endswith("-baseline"):
            continue
        prefix = name.removesuffix("-baseline")
        control_name = next(n for n in worlds if n.startswith(prefix + "-without-sparse"))
        control = worlds[control_name]
        difference = [
            sum(
                primary(r)[metric] if metric == "covered_blocks" else primary(r)[metric]["count"]
                for r in control["routes"].values()
            )
            - sum(
                primary(r)[metric] if metric == "covered_blocks" else primary(r)[metric]["count"]
                for r in baseline["routes"].values()
            )
            for metric in ("adjacent", "geometric_visible", "covered_blocks")
        ]
        lines.append(
            f"| {prefix.removeprefix('full-')} | {difference[0]} | {difference[1]} | {difference[2]} |"  # noqa: E501 - generated Markdown row
        )
    lines += [
        "",
        "## Scope and input identities",
        "",
        "Placement densities are retained per world in the raw result and remain Item 10 quantities.",  # noqa: E501 - generated Markdown row
        "Adjacency is distinct from ray-clear targets, which are distinct from modeled access.",
        "Speeds (walking 4 [3,5], horse 7 [5,9], boat 8 [6,10] blocks/second) are assumptions.",
        "Infeasible completed costs are null. Prefix and unconstrained costs remain separately labeled.",  # noqa: E501 - generated Markdown row
        "Repeated-family events do not demonstrate identical generated layouts. Missing targets and",  # noqa: E501 - generated Markdown row
        "geometry retain UNKNOWN outcomes; zeroes and censored gaps do not establish global absence.",  # noqa: E501 - generated Markdown row
        "Human recognition, actual fights, meaningful-interaction time, enjoyment and human",
        "Adventure Activity Ratio are **NOT MEASURED**. No Item 12 result is claimed.",
        "",
        "| Result | SHA-256 |",
        "| --- | --- |",
    ]
    lines += [
        f"| [results/{n}.json.gz](results/{n}.json.gz) | `{digest}` |"
        for n, digest in hashes.items()
    ]
    lines += [
        "",
        "## Complete gap and repetition statistics",
        "",
        "All sixteen worlds, four routes, three radii, three windows, ten categories and two",
        "independent populations are reported below: 11,520 rows. Distances are horizontal blocks.",
        "Distribution cells give n; median; inclusive IQR; [minimum, maximum], rounded to two decimals.",  # noqa: E501 - report prose
        "NA means no intervals, not a measured zero. Gap distributions use successive candidate",
        "locations; boundary gaps are separately right/left censored. With no candidate, the",
        "single boundary entry is the entire empty window. Maximum empty includes boundaries.",
        "First repeat is distance from route start; NR@window is right censoring. Same-position",
        "ties and zero repeat intervals remain. Counts are overlapping route/category memberships.",
        "Each mode's repeat-time cell gives n, central-speed median/IQR/range and the speed envelope.",  # noqa: E501 - report prose
        "Time values are unconstrained modeled seconds, including for infeasible modes; the speed",
        "envelope is assumption sensitivity, not a confidence interval. NR uses that row's window.",
        "Individual events, family identities and unrounded values remain in the linked results.",
        "",
    ]
    for name, world in worlds.items():
        lines += [
            f"### {name.removeprefix('full-')}",
            "",
            "| Route | Radius | Window | Category | Population | Locations | Families | Gap distribution | Censored boundary gaps | Maximum empty | Repeats | First repeat | Repeat-interval distribution | Walking repeat seconds | Horse repeat seconds | Boat repeat seconds |",  # noqa: E501 - generated Markdown row
            "| --- | ---: | ---: | --- | --- | ---: | ---: | --- | --- | ---: | ---: | --- | --- | --- | --- | --- |",  # noqa: E501 - generated Markdown row
        ]
        for label, route in world["routes"].items():
            for row in route["summaries"]:
                for population in ("adjacent", "geometric_visible"):
                    stats = row[population]
                    boundaries = ", ".join(f"{v:.2f}" for v in stats["censored_boundary_gaps"])
                    first = (
                        f"{stats['first_repeat_distance']:.2f}"
                        if stats["first_repeat_distance"] is not None
                        else f"NR@{stats['no_repeat_right_censored_at']}"
                    )
                    time_key = "adjacent_time" if population == "adjacent" else "visible_time"
                    times = " | ".join(row["modes"][mode][time_key] for mode in SPEEDS)
                    lines.append(
                        f"| {label} | {row['radius']} | {row['window']} | {row['category']} | {population} | {stats['count']} | {stats['unique_families']} | {distribution_text(stats['gap_distribution'])} | [{boundaries}] | {stats['maximum_empty_interval']:.2f} | {stats['repeat_count']} | {first} | {distribution_text(stats['repeat_interval_distribution'])} | {times} |"  # noqa: E501 - generated Markdown row
                    )
        lines.append("")
    lines += [
        "## Reachable-prefix geometric opportunity coverage",
        "",
        "All 5,760 world/route/radius/window/category rows, each with three transport modes.",
        "Each mode cell is covered blocks / reachable-prefix blocks. Only sampled eight-block",
        "segments wholly within the prefix contribute to its geometric coverage numerator.",
        "0/0 means no modeled reachable distance; its coverage ratio is undefined, not zero percent.",  # noqa: E501 - report prose
        "An infeasible full route may still have a nonempty prefix. These modeled reachable",
        "opportunities are separate from full-route geometry and are not observed interactions.",
        "Each cost cell gives completed / prefix / unconstrained seconds, with central [fast, slow]",  # noqa: E501 - report prose
        "speed values. Completed cost is null for an infeasible/unknown full-route mode even when",
        "a shorter prefix is reachable. The transport reason codes are listed above.",
        "",
    ]
    for name, world in worlds.items():
        lines += [
            f"### {name.removeprefix('full-')} reachable coverage",
            "",
            "| Route | Radius | Window | Category | Walking coverage | Horse coverage | Boat coverage | Walking cost seconds | Horse cost seconds | Boat cost seconds |",  # noqa: E501 - generated Markdown row
            "| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for label, route in world["routes"].items():
            for row in route["summaries"]:
                cells = [
                    f"{row['modes'][mode]['prefix_covered_blocks']}/{row['modes'][mode]['prefix_denominator_blocks']}"
                    for mode in SPEEDS
                ]
                costs = [
                    " / ".join(
                        cost_text(row["modes"][mode][key])
                        for key in ("completed_cost", "prefix_cost", "unconstrained_cost")
                    )
                    for mode in SPEEDS
                ]
                lines.append(
                    f"| {label} | {row['radius']} | {row['window']} | {row['category']} | {' | '.join(cells)} | {' | '.join(costs)} |"  # noqa: E501 - generated Markdown row
                )
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    text = build(args.results)
    with args.output.open("x") as stream:
        _ = stream.write(text)


if __name__ == "__main__":
    main()
