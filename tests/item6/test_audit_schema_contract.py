# pyright: standard
"""Characterize the Item 6 audit schema boundary."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import ValidationError

from tests.item6.helpers import AUDIT, FROZEN, MANIFEST, validate

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize(
    ("anchor", "unexpected_field"),
    [
        ("{\n", '  "unexpected_top_level": true,\n'),
        ('  "systems": [\n    {\n', '      "unexpected_system_field": true,\n'),
        ('  "settings": [\n    {\n', '      "unexpected_setting_field": true,\n'),
        ('      "evidence": {\n', '        "unexpected_evidence_field": true,\n'),
        (
            '          {\n            "line": 10,\n',
            '            "unexpected_observation_field": true,\n',
        ),
        ('  "findings": [\n    {\n', '      "unexpected_finding_field": true,\n'),
        ('  "file_accounting": [\n    {\n', '      "unexpected_classification_field": true,\n'),
    ],
)
def test_validate_rejects_unknown_audit_fields(
    tmp_path: Path, anchor: str, unexpected_field: str
) -> None:
    # Given: a syntactically valid audit with one unknown object member.
    audit_path = tmp_path / "audit-with-unknown-field.json"
    audit_path.write_text(
        AUDIT.read_text(encoding="utf-8").replace(anchor, f"{anchor}{unexpected_field}", 1),
        encoding="utf-8",
    )

    # When/Then: validation refuses every unknown audit-boundary field.
    with pytest.raises(ValidationError, match="extra_forbidden"):
        validate(FROZEN, MANIFEST, audit_path)
