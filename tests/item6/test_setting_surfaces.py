# pyright: standard
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

import pytest

from mcpack_evidence.item6_surface_validation import (
    SurfaceValidationError,
    build_setting_surface,
    parse_cristellib_json5,
)
from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate

AUDIT_DATA = json.loads(AUDIT.read_text(encoding="utf-8"))
GENERATOR_SPEC = importlib.util.spec_from_file_location(
    "generate_item6_setting_surfaces", Path("tools/generate_item6_setting_surfaces.py")
)
assert GENERATOR_SPEC is not None
assert GENERATOR_SPEC.loader is not None
GENERATOR = ModuleType(GENERATOR_SPEC.name)
GENERATOR_SPEC.loader.exec_module(GENERATOR)


def test_parser_extracts_nested_typed_leaves_with_exact_lines(tmp_path: Path) -> None:
    # Given: nested CristelLib-style JSON5 with every supported scalar class.
    source = tmp_path / "nested.json5"
    source.write_text(
        '{\n  "outer": {\n    "bool": true,\n    "integer": -2,\n'
        '    "decimal": 1.25e+2,\n    "text": "value"\n  }\n}\n',
        encoding="utf-8",
    )

    # When: the strict parser extracts the scalar leaves.
    leaves = parse_cristellib_json5(source)

    # Then: full paths, exact lines, syntax framing, values, and types are retained.
    assert [(leaf.key, leaf.line, leaf.prefix, leaf.suffix, leaf.value) for leaf in leaves] == [
        ("outer.bool", 3, '"bool": ', ",", True),
        ("outer.integer", 4, '"integer": ', ",", -2),
        ("outer.decimal", 5, '"decimal": ', ",", 125.0),
        ("outer.text", 6, '"text": ', "", "value"),
    ]


@pytest.mark.parametrize(
    "contents",
    [
        '{\n  "group": {\n    "same": true,\n    "same": false\n  }\n}\n',
        '{\n  "group": {\n    unsupported\n  }\n}\n',
        '{\n  "group": {\n    "value": true\n}\n',
    ],
)
def test_parser_rejects_duplicates_and_malformed_input(tmp_path: Path, contents: str) -> None:
    # Given: malformed or duplicate CristelLib-style input.
    source = tmp_path / "invalid.json5"
    source.write_text(contents, encoding="utf-8")

    # When/Then: parsing fails instead of silently dropping source data.
    with pytest.raises(SurfaceValidationError):
        parse_cristellib_json5(source)


def test_generator_is_deterministic_and_cli_matches_function(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    # Given: one real CristelLib source file and fixed arguments.
    relative = "config/cristellib/dungeons_arise_seven_seas/structure_placement_config.json5"

    # When: generation runs repeatedly and through the CLI entry point.
    first = GENERATOR.generate(FROZEN, "WDA Seven Seas", [relative])
    second = GENERATOR.generate(FROZEN, "WDA Seven Seas", [relative])
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "tools/generate_item6_setting_surfaces.py",
            "--root",
            str(FROZEN),
            "--system",
            "WDA Seven Seas",
            "--file",
            relative,
        ],
    )
    exit_code = GENERATOR.main()

    # Then: the pure generation result is byte-for-byte deterministic.
    assert first == second
    assert json.loads(first) == [
        build_setting_surface("WDA Seven Seas", relative, FROZEN / relative)
    ]
    assert exit_code == 0
    assert capsys.readouterr().out == first


def test_grouped_surface_contract_validates() -> None:
    # Given/When/Then: schema v2 requires and validates its grouped-surface collection.
    assert AUDIT_DATA["schema_version"] == "item6-config-audit-v2"
    assert isinstance(AUDIT_DATA["setting_surfaces"], list)
    validate(FROZEN, MANIFEST, AUDIT)
