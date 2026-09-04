# pyright: standard
"""Contract tests for the Item 6 capture sanitization receipt."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item6_sanitization import (
    SanitizationReceipt,
    SanitizationReceiptValidationError,
    validate_sanitization_receipt,
)

if TYPE_CHECKING:
    from pathlib import Path

_SENTINEL = "<redacted-generated-secret>"


def _make_valid_fixture(tmp_path: Path) -> tuple[Path, Path]:
    """Create one frozen root and its adjacent valid sanitization receipt."""
    frozen_root = tmp_path / "frozen"
    target = frozen_root / "config" / "resourceful-config-web.json"
    target.parent.mkdir(parents=True)
    _ = target.write_text(
        json.dumps({"validator": {"if": {"password": _SENTINEL}}}), encoding="utf-8"
    )
    receipt = tmp_path / "config-sanitization.json"
    _ = receipt.write_text(
        json.dumps(
            {
                "schema_version": "item6-config-sanitization-v1",
                "sanitized_file_count": 1,
                "redaction_count": 1,
                "files": [
                    {
                        "path": "config/resourceful-config-web.json",
                        "redactions": [
                            {
                                "json_pointer": "/validator/if/password",
                                "replacement": _SENTINEL,
                                "value_type": "string",
                            }
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return receipt, frozen_root


def test_validate_sanitization_receipt_returns_typed_bound_receipt(tmp_path: Path) -> None:
    """A complete receipt binds the sentinel to the real frozen JSON target."""
    # Given: a regular receipt and frozen target with the redaction sentinel.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)

    # When: phase B parses and validates the receipt boundary.
    receipt = validate_sanitization_receipt(receipt_path, frozen_root)

    # Then: callers receive the immutable typed receipt.
    assert isinstance(receipt, SanitizationReceipt)
    assert receipt.files[0].redactions[0].replacement == _SENTINEL


@pytest.mark.parametrize(
    ("mutation", "value"),
    [
        ("unknown", True),
        ("unknown_file", True),
        ("unknown_redaction", True),
        ("missing", None),
        ("sanitized_file_count", 2),
        ("redaction_count", 2),
        ("path", "config/other.json"),
        ("json_pointer", "/validator/if/other"),
        ("replacement", "<wrong-sentinel>"),
        ("value_type", "number"),
    ],
)
def test_validate_sanitization_receipt_rejects_contract_mutations(
    tmp_path: Path, mutation: str, value: bool | int | str | None
) -> None:
    """Receipt schema mutations fail closed before callers receive typed data."""
    # Given: one valid receipt with exactly one adversarial contract mutation.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    match mutation:
        case "unknown":
            receipt["unexpected"] = value
        case "unknown_file":
            receipt["files"][0]["unexpected"] = value
        case "unknown_redaction":
            receipt["files"][0]["redactions"][0]["unexpected"] = value
        case "missing":
            del receipt["files"][0]["redactions"][0]["value_type"]
        case "sanitized_file_count" | "redaction_count":
            receipt[mutation] = value
        case "path":
            receipt["files"][0]["path"] = value
        case "json_pointer" | "replacement" | "value_type":
            receipt["files"][0]["redactions"][0][mutation] = value
        case unreachable:
            pytest.fail(f"unexpected mutation: {unreachable}")
    _ = receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

    # When/Then: strict parsing rejects the altered evidence contract.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_malformed_json(tmp_path: Path) -> None:
    """Receipt JSON syntax is an untrusted boundary, not a best-effort input."""
    # Given: a malformed receipt beside a valid frozen root.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    _ = receipt_path.write_text("{", encoding="utf-8")

    # When/Then: parsing fails with the receipt-specific error type.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_missing_receipt(tmp_path: Path) -> None:
    """An absent receipt has no evidence value."""
    # Given: a frozen root whose expected receipt does not exist.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    receipt_path.unlink()

    # When/Then: validation rejects the absent receipt.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_symlinked_receipt(tmp_path: Path) -> None:
    """Receipt indirection cannot escape the evidence boundary."""
    # Given: a receipt path replaced by a symlink to an otherwise-valid file.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    target = tmp_path / "external-receipt.json"
    receipt_path.replace(target)
    receipt_path.symlink_to(target)

    # When/Then: validation rejects the symlink rather than following it.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_missing_target(tmp_path: Path) -> None:
    """A receipt cannot bind a target that is absent from the frozen root."""
    # Given: a valid receipt with its required frozen JSON target removed.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    (frozen_root / "config" / "resourceful-config-web.json").unlink()

    # When/Then: validation rejects the missing target.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_target_without_sentinel(tmp_path: Path) -> None:
    """A syntactically valid target still fails when its pointer is not redacted."""
    # Given: the required target exists but does not contain the redaction sentinel.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    target = frozen_root / "config" / "resourceful-config-web.json"
    _ = target.write_text(
        json.dumps({"validator": {"if": {"password": "wrong"}}}), encoding="utf-8"
    )

    # When/Then: validation rejects an unbound receipt.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)


def test_validate_sanitization_receipt_rejects_symlinked_target(tmp_path: Path) -> None:
    """A receipt cannot bind a target that resolves through a symlink."""
    # Given: the required frozen target is replaced by a symlink.
    receipt_path, frozen_root = _make_valid_fixture(tmp_path)
    target = frozen_root / "config" / "resourceful-config-web.json"
    external = tmp_path / "external-resourceful-config-web.json"
    target.replace(external)
    target.symlink_to(external)

    # When/Then: validation rejects the symlink rather than following it.
    with pytest.raises(SanitizationReceiptValidationError):
        validate_sanitization_receipt(receipt_path, frozen_root)
