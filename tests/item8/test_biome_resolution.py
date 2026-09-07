from __future__ import annotations

from mcpack_evidence.item7_restrictions import resolve_biome_tag


def test_runtime_registry_excludes_absent_optional_compatibility_biomes() -> None:
    tags: dict[str, list[object]] = {
        "example:mineshaft": [
            "minecraft:plains",
            {"id": "absentmod:forest", "required": False},
            {"id": "#absentmod:forests", "required": False},
            "#example:caves",
        ],
        "example:caves": ["minecraft:lush_caves"],
    }
    registered = frozenset({"minecraft:plains", "minecraft:lush_caves"})
    resolved, missing = resolve_biome_tag("example:mineshaft", tags, registered_biomes=registered)
    assert resolved == set(registered)
    assert missing == ()
    packaged, _ = resolve_biome_tag("example:mineshaft", tags)
    assert "absentmod:forest" in packaged


def test_absent_required_biome_remains_an_explicit_failure() -> None:
    tags: dict[str, list[object]] = {
        "example:root": ["#example:child"],
        "example:child": ["minecraft:plains", "absentmod:forest"],
    }
    resolved, missing = resolve_biome_tag(
        "example:root", tags, registered_biomes=frozenset({"minecraft:plains"})
    )
    assert resolved == set()
    assert missing == ("absentmod:forest",)


def test_optional_invalid_nested_tag_does_not_leak_its_partial_contents() -> None:
    tags: dict[str, list[object]] = {
        "example:root": [{"id": "#example:child", "required": False}],
        "example:child": ["minecraft:plains", "absentmod:forest"],
    }
    resolved, missing = resolve_biome_tag(
        "example:root", tags, registered_biomes=frozenset({"minecraft:plains"})
    )
    assert resolved == set()
    assert missing == ()


def test_tag_cycle_stays_unresolved_with_runtime_filtering() -> None:
    tags: dict[str, list[object]] = {"example:a": ["#example:b"], "example:b": ["#example:a"]}
    resolved, missing = resolve_biome_tag("example:a", tags, registered_biomes=frozenset())
    assert resolved == set()
    assert missing == ("example:a",)
