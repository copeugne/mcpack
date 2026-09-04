# ruff: noqa: EM101, TRY003
"""Parse and bind the Item 6 evidence-safe capture sanitization receipt."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import ClassVar, Final, Literal, TypedDict

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json

_SENTINEL: Final = "<redacted-generated-secret>"
_TARGET_PATH: Final = Path("config/resourceful-config-web.json")
_CANONICAL_RECEIPT: Final = "evidence/item-6/config-sanitization.json"


class SanitizationMetadata(TypedDict):
    """Manifest metadata binding the canonical sanitization receipt."""

    receipt: str
    sha256: str
    sanitized_file_count: int
    redaction_count: int


class SanitizationRedaction(BaseModel):
    """The sole permitted Item 6 generated-credential replacement."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    json_pointer: Literal["/validator/if/password"]
    replacement: Literal["<redacted-generated-secret>"]
    value_type: Literal["string"]


class SanitizedFile(BaseModel):
    """The sole permitted frozen file that may contain the replacement."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    path: Literal["config/resourceful-config-web.json"]
    redactions: tuple[SanitizationRedaction]


class SanitizationReceipt(BaseModel):
    """Strict evidence-safe record of the one generated-credential redaction."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    schema_version: Literal["item6-config-sanitization-v1"]
    sanitized_file_count: Literal[1]
    redaction_count: Literal[1]
    files: tuple[SanitizedFile]


class _ResourcefulValidatorIf(BaseModel):
    """Nested target shape that proves the generated credential was redacted."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow", strict=True)

    password: str


class _ResourcefulValidator(BaseModel):
    """Validator section retaining unrelated Resourceful configuration fields."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow", strict=True)

    if_: _ResourcefulValidatorIf = Field(alias="if")


class _ResourcefulConfig(BaseModel):
    """Resourceful configuration boundary required by this receipt contract."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow", strict=True)

    validator: _ResourcefulValidator


class SanitizationReceiptValidationError(ValueError):
    """Raised when sanitization evidence is unsafe, malformed, or unbound."""


_RECEIPT_ADAPTER: Final[TypeAdapter[SanitizationReceipt]] = TypeAdapter(SanitizationReceipt)


def validate_sanitization_receipt(receipt_path: Path, frozen_root: Path) -> SanitizationReceipt:
    """Return a strictly parsed receipt only when its target has the exact sentinel."""
    _require_regular_file(receipt_path, "sanitization receipt")
    try:
        receipt_bytes = receipt_path.read_bytes()
        _ = parse_strict_json(receipt_bytes)
        receipt = _RECEIPT_ADAPTER.validate_json(receipt_bytes, strict=True, extra="forbid")
    except (StrictJsonError, ValidationError):
        raise SanitizationReceiptValidationError("sanitization receipt is malformed") from None
    target = _resolve_target(frozen_root)
    try:
        configuration = _ResourcefulConfig.model_validate(
            parse_strict_json(target.read_bytes()), strict=True
        )
    except (StrictJsonError, ValidationError):
        raise SanitizationReceiptValidationError("sanitized target JSON is malformed") from None
    if configuration.validator.if_.password != _SENTINEL:
        raise SanitizationReceiptValidationError(
            "sanitized target does not contain the redaction sentinel"
        )
    return receipt


def validate_sanitization_binding(
    manifest_path: Path, frozen_root: Path, metadata: SanitizationMetadata
) -> None:
    """Bind manifest sanitization metadata to the canonical receipt and frozen target."""
    if metadata["receipt"] != _CANONICAL_RECEIPT:
        raise SanitizationReceiptValidationError(
            "sanitization receipt must name the canonical repository path"
        )
    receipt_path = manifest_path.parent / "config-sanitization.json"
    try:
        receipt = validate_sanitization_receipt(receipt_path, frozen_root)
    except SanitizationReceiptValidationError as error:
        raise SanitizationReceiptValidationError(
            "sanitization receipt binding is invalid"
        ) from error
    if _sha256(receipt_path) != metadata["sha256"]:
        raise SanitizationReceiptValidationError(
            "sanitization receipt digest does not match manifest"
        )
    if (
        receipt.sanitized_file_count != metadata["sanitized_file_count"]
        or receipt.redaction_count != metadata["redaction_count"]
    ):
        raise SanitizationReceiptValidationError(
            "sanitization receipt counts do not match manifest"
        )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require_regular_file(path: Path, name: str) -> None:
    """Require an existing file that is not itself a symlink."""
    if path.is_symlink() or not path.is_file():
        message = f"{name} must be a real non-symlink file"
        raise SanitizationReceiptValidationError(message)


def _resolve_target(frozen_root: Path) -> Path:
    """Resolve the required target while rejecting symlinked frozen-root components."""
    if frozen_root.is_symlink() or not frozen_root.is_dir():
        raise SanitizationReceiptValidationError("frozen root must be a real non-symlink directory")
    root_resolved = frozen_root.resolve(strict=True)
    target = frozen_root
    for component in _TARGET_PATH.parts:
        target /= component
        if target.is_symlink():
            raise SanitizationReceiptValidationError(
                "sanitized target must be a real non-symlink file"
            )
    if not target.is_file():
        raise SanitizationReceiptValidationError("sanitized target must be a real non-symlink file")
    try:
        _ = target.resolve(strict=True).relative_to(root_resolved)
    except ValueError:
        raise SanitizationReceiptValidationError(
            "sanitized target must remain under frozen root"
        ) from None
    return target
