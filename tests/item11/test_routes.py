# pyright: standard
"""Focused checks for route geometry, censoring, transport and accepted input custody."""

import gzip
import hashlib
import json
import shutil
import subprocess
from array import array
from pathlib import Path

import pytest
from tools import analyze_route_opportunities as routes
from tools.manage_item4_environment import _world_backup_lock


def test_height_field_occlusion_and_missing() -> None:
    heights = array("h", [0]) * 1024**2
    assert routes.ray(heights, 0, 0, [10, 3, 0]) == "RAY_CLEAR"
    heights[512 * 1024 + 517] = 5
    assert routes.ray(heights, 0, 0, [10, 3, 0]) == "OCCLUDED"
    heights[512 * 1024 + 517] = routes.MISSING
    assert routes.ray(heights, 0, 0, [10, 3, 0]) == "UNKNOWN"
    assert routes.ray(heights, 0, 0, None) == "UNKNOWN"
    assert routes.height_at(heights, -513, 0) is None


def test_event_ties_repetition_and_boundaries() -> None:
    summary = routes.event_summary([(20, "a", "2"), (10, "a", "1"), (20, "b", "3")], 256)
    assert summary["gaps"] == [10, 0]
    assert summary["repeat_count"] == 1
    assert summary["first_repeat_distance"] == 20
    assert summary["repeats"][0]["interval"] == 10
    assert summary["censored_boundary_gaps"] == [10, 236]
    assert summary["maximum_empty_interval"] == 236
    assert routes.event_summary([], 256)["no_repeat_right_censored_at"] == 256


def test_transport_does_not_switch_to_swimming() -> None:
    route = (0, 0, 1, 0)
    tops = {
        (x, z): {"height": 62, "state": {"Name": "minecraft:water"}}
        for x in range(-1, 770)
        for z in (-1, 0, 1)
    }
    boat = routes.model_transport(route, "boat", tops)
    assert boat["status"] == "MODEL_FEASIBLE"
    assert boat["reachable_prefix"] == 768
    walking = routes.model_transport(route, "walking", tops)
    assert walking["status"] == "INFEASIBLE"
    assert walking["reachable_prefix"] == 0
    tops[(101, 1)]["state"] = {"Name": "minecraft:stone"}
    boat = routes.model_transport(route, "boat", tops)
    assert boat["reachable_prefix"] == 99
    assert boat["failures"][0]["distance"] == 100


def test_dry_steps_fail_and_missing_state_is_unknown() -> None:
    route = (0, 0, 1, 0)
    tops = {(x, 0): {"height": 62, "state": {"Name": "minecraft:stone"}} for x in range(769)}
    tops[(10, 0)]["height"] = 64
    horse = routes.model_transport(route, "horse", tops)
    assert horse["status"] == "INFEASIBLE"
    assert horse["reachable_prefix"] == 9
    assert [r["distance"] for r in horse["failures"]] == [10, 11]
    tops[(10, 0)]["height"] = 62
    tops[(10, 0)] = {"height": 62, "state": None}
    assert routes.model_transport(route, "walking", tops)["status"] == "UNKNOWN"


def test_complete_inventory_rejects_omission_and_link(tmp_path: Path) -> None:
    (tmp_path / "data").write_bytes(b"world")
    digest = hashlib.sha256(b"world").hexdigest()
    manifest = [{"path": "data", "size_bytes": 5, "sha256": digest}]
    routes.verify_world(tmp_path, manifest)
    (tmp_path / "extra").write_bytes(b"new")
    with pytest.raises(ValueError, match="inventory"):
        routes.verify_world(tmp_path, manifest)
    (tmp_path / "extra").unlink()
    (tmp_path / "linked").symlink_to(tmp_path / "data")
    with pytest.raises(ValueError, match="symlink"):
        routes.verify_world(tmp_path, manifest)


def test_bound_input_rejects_changed_bytes(tmp_path: Path) -> None:
    source = tmp_path / "data"
    source.write_bytes(b"new")
    with pytest.raises(ValueError, match="identity mismatch"):
        routes.read_bound(source, "0" * 64)


def test_fixed_route_disks_do_not_escape_saved_frame() -> None:
    assert len(routes.ROUTES) == 4
    for route in routes.ROUTES.values():
        for distance in range(769):
            x, z = routes.point(route, distance)
            assert -512 <= x - 96 <= x + 96 < 512
            assert -512 <= z - 96 <= z + 96 < 512


def test_coverage_deduplicates_locations_and_censors_window() -> None:
    observation = {
        "projection": 100,
        "adjacent_distance": 32,
        "family_id": "a",
        "location_id": "a1",
        "role": "T2",
        "comparison_groups": [],
        "rays": [
            {"distance": 4, "target_distance": 32, "result": "RAY_CLEAR"},
            {"distance": 12, "target_distance": 32, "result": "RAY_CLEAR"},
        ],
    }
    other = {**observation, "location_id": "a2", "projection": 256}
    models = {
        mode: {
            "status": "INFEASIBLE",
            "reachable_prefix": 9,
            "cumulative_cost_distance": list(range(769)),
        }
        for mode in routes.SPEEDS
    }
    summaries = routes.summarize_route([observation, other], models)
    row = next(
        r for r in summaries if r["radius"] == 32 and r["window"] == 256 and r["category"] == "T2"
    )
    assert row["adjacent"]["count"] == 1
    assert row["geometric_visible"]["count"] == 2
    assert row["covered_blocks"] == 16
    assert row["denominator_blocks"] == 256
    assert row["modes"]["walking"]["completed_cost"] is None
    assert row["modes"]["walking"]["prefix_covered_blocks"] == 8


def test_inventory_check_preserves_java_compatible_lock(tmp_path: Path) -> None:
    probe = """
import fcntl,sys
with open(sys.argv[1], "r+b") as stream:
    try:
        fcntl.lockf(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(23)
sys.exit(0)
"""
    uv = shutil.which("uv")
    assert uv is not None
    with _world_backup_lock(tmp_path):
        routes.verify_world(tmp_path, [])
        result = subprocess.run(  # noqa: S603 - fixed lock probe and test-owned path
            [uv, "run", "--no-sync", "python", "-c", probe, str(tmp_path / "session.lock")],
            check=False,
        )
        assert result.returncode == 23, "inventory verification released the held world lock"


def test_visibility_target_beyond_anchor_cutoff_is_retained() -> None:
    heights = array("h", [0]) * 1024**2
    row = {
        "location_id": "fixture",
        "family_id": "fixture",
        "role": "T2",
        "comparison_groups": [],
        "anchor_x": 10,
        "anchor_z": 120,
        "target": [10, 3, 0],
    }
    observations = routes.route_observations((0, 0, 1, 0), [row], heights)
    assert len(observations) == 1
    assert observations[0]["adjacent_distance"] == 120
    models = {
        mode: {
            "status": "MODEL_FEASIBLE",
            "reachable_prefix": 768,
            "cumulative_cost_distance": list(range(769)),
        }
        for mode in routes.SPEEDS
    }
    summary = next(
        r
        for r in routes.summarize_route(observations, models)
        if (r["radius"], r["window"], r["category"]) == (32, 256, "T2")
    )
    assert summary["adjacent"]["count"] == 0
    assert summary["geometric_visible"]["count"] == 1


def test_retained_outpost_visibility_is_not_anchor_adjacency() -> None:
    source = routes.ROOT / "evidence/item-11/results/full-biome-diverse-r1-without-sparse.json.gz"
    route = json.loads(gzip.decompress(source.read_bytes()))["routes"]["east-north"]
    identity = "repurposed_structures:outpost_desert@13,20"
    outpost = next(r for r in route["observations"] if r["location_id"] == identity)
    assert outpost["adjacent_distance"] == 72
    assert any(r["result"] == "RAY_CLEAR" and r["target_distance"] < 64 for r in outpost["rays"])
    summary = next(
        r
        for r in routes.summarize_route(route["observations"], route["transport"])
        if (r["radius"], r["window"], r["category"]) == (64, 768, "all_locations")
    )
    assert identity not in {e[2] for e in summary["adjacent"]["events"]}
    assert identity in {e[2] for e in summary["geometric_visible"]["events"]}


def test_infeasible_route_never_reports_completed_window_cost() -> None:
    source = routes.ROOT / "evidence/item-11/results/full-ocean-heavy-r1-without-sparse.json.gz"
    route = json.loads(gzip.decompress(source.read_bytes()))["routes"]["east-south"]
    assert route["transport"]["boat"]["status"] == "INFEASIBLE"
    assert route["transport"]["boat"]["reachable_prefix"] == 756
    summaries = routes.summarize_route(route["observations"], route["transport"])
    for row in summaries:
        assert row["modes"]["boat"]["completed_cost"] is None
        assert row["modes"]["boat"]["prefix_cost"] is not None
        assert row["modes"]["boat"]["unconstrained_cost"] is not None
