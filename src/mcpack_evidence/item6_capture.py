"""Item 6 configuration capture boundary."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from typing import ClassVar, Final, Literal

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item6_capture_sanitization import (
    SourceSanitizationError,
    redact_generated_credential,
)

_DIRECTORIES: Final = ("config", "defaultconfigs", "world", "world/serverconfig")
_RESOURCEFUL_CONFIG_PATH: Final = "config/resourceful-config-web.json"
_RESOURCEFUL_CONFIG: Final = Path(_RESOURCEFUL_CONFIG_PATH)
_SANITIZATION_RECEIPT: Final = "config-sanitization.json"
_REDACTION_SENTINEL: Final = "<redacted-generated-secret>"


class _ReceiptRedaction(BaseModel):
    """One evidence-safe replacement recorded by the sanitization receipt."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    json_pointer: Literal["/validator/if/password"] = "/validator/if/password"
    replacement: Literal["<redacted-generated-secret>"] = _REDACTION_SENTINEL
    value_type: Literal["string"] = "string"


class _ReceiptFile(BaseModel):
    """One sanitized file recorded without its source credential or identity."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    path: Literal["config/resourceful-config-web.json"] = _RESOURCEFUL_CONFIG_PATH
    redactions: tuple[_ReceiptRedaction, ...] = (_ReceiptRedaction(),)


class _SanitizationReceipt(BaseModel):
    """Evidence-safe receipt for the capture-side generated credential replacement."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    schema_version: Literal["item6-config-sanitization-v1"] = "item6-config-sanitization-v1"
    sanitized_file_count: Literal[1] = 1
    redaction_count: Literal[1] = 1
    files: tuple[_ReceiptFile, ...] = (_ReceiptFile(),)


class CaptureValidationError(ValueError):
    """Raised when an Item 6 capture source violates its filesystem contract."""


def capture(instance: Path, output: Path) -> None:
    """Copy configuration-bearing paths without altering the source instance."""
    _require_real_output_parent(output.parent)
    receipt = output.parent / _SANITIZATION_RECEIPT
    if output == receipt:
        message = "output path collides with sanitization receipt"
        raise CaptureValidationError(message)
    if output.exists() or output.is_symlink():
        message = f"output already exists: {output}"
        raise FileExistsError(message)
    if receipt.exists() or receipt.is_symlink():
        message = f"sanitization receipt already exists: {receipt}"
        raise FileExistsError(message)
    _require_directory(instance, "instance")
    _require_external_destinations(instance, output, receipt)
    sources = tuple(instance / relative for relative in _DIRECTORIES)
    for source, relative in zip(sources, _DIRECTORIES, strict=True):
        _require_directory(source, relative)
        _require_no_nested_symlinks(source, relative)
    properties = instance / "server.properties"
    _require_regular_file(properties, "server.properties")
    resourceful_config = instance / _RESOURCEFUL_CONFIG
    _require_regular_file(resourceful_config, _RESOURCEFUL_CONFIG.as_posix())
    sanitized_resourceful_config = _sanitize_resourceful_config(resourceful_config)

    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.capture-", dir=output.parent))
    try:
        _copy_configuration_tree(
            instance / "config", staging / "config", sanitized_resourceful_config
        )
        for source, target in (
            (instance / "defaultconfigs", staging / "defaultconfigs"),
            (instance / "world" / "serverconfig", staging / "world-serverconfig"),
        ):
            _ = shutil.copytree(source, target)
        _ = shutil.copy2(properties, staging / "server.properties")
        staged_receipt = staging / _SANITIZATION_RECEIPT
        _ = staged_receipt.write_text(
            _SanitizationReceipt().model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        _ = staging.replace(output)
        _ = (output / _SANITIZATION_RECEIPT).replace(receipt)
    finally:
        if staging.exists():
            _ = shutil.rmtree(staging)


def _sanitize_resourceful_config(path: Path) -> bytes:
    """Strictly verify and redact only the generated web-validator credential."""
    try:
        return redact_generated_credential(path.read_bytes())
    except SourceSanitizationError:
        message = f"invalid generated credential shape: {_RESOURCEFUL_CONFIG.as_posix()}"
        raise CaptureValidationError(message) from None


def _copy_configuration_tree(
    source: Path, target: Path, sanitized_resourceful_config: bytes
) -> None:
    """Copy configuration while replacing the sensitive target before it reaches staging."""

    def ignore_resourceful_config(directory: str, names: list[str]) -> set[str]:
        """Exclude only the root resourceful configuration file from the byte copy."""
        if Path(directory) == source and _RESOURCEFUL_CONFIG.name in names:
            return {_RESOURCEFUL_CONFIG.name}
        return set()

    _ = shutil.copytree(source, target, ignore=ignore_resourceful_config)
    _ = (target / _RESOURCEFUL_CONFIG.name).write_bytes(sanitized_resourceful_config)


def _require_directory(path: Path, name: str) -> None:
    """Require one real, non-symlink source directory."""
    if path.is_symlink() or not path.is_dir():
        message = f"required directory must be a real non-symlink directory: {name}"
        raise CaptureValidationError(message)


def _require_regular_file(path: Path, name: str) -> None:
    """Require one real, non-symlink source file."""
    if path.is_symlink() or not path.is_file():
        message = f"required regular non-symlink file is invalid: {name}"
        raise CaptureValidationError(message)


def _require_real_output_parent(path: Path) -> None:
    """Reject an existing symlink in the lexical output parent chain."""
    candidate = path
    while True:
        if candidate.is_symlink():
            message = f"output parent contains a symlink: {path}"
            raise CaptureValidationError(message)
        if candidate == candidate.parent:
            return
        candidate = candidate.parent


def _require_no_nested_symlinks(path: Path, name: str) -> None:
    """Reject symlink entries within one source tree before copying starts."""
    for candidate in path.rglob("*"):
        if candidate.is_symlink():
            message = f"required source tree contains a symlink: {name}"
            raise CaptureValidationError(message)


def _require_external_destinations(instance: Path, *destinations: Path) -> None:
    instance_root = instance.resolve(strict=True)
    for destination in destinations:
        try:
            _ = destination.resolve(strict=False).relative_to(instance_root)
        except ValueError:
            continue
        message = "capture destinations must remain outside the source instance"
        raise CaptureValidationError(message)
