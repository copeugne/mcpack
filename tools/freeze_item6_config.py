#!/usr/bin/env python3
"""Freeze and validate the untouched Item 6 generated configuration baseline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, TypeAdapter

from mcpack_evidence.item6_capture import capture
from mcpack_evidence.item6_validation import sha256, validate

__all__ = ("capture", "sha256", "validate")


class _CaptureArguments(BaseModel, frozen=True):
    command: Literal["capture"]
    instance: Path
    output: Path

    def run(self) -> int:
        capture(self.instance, self.output)
        return 0


class _ValidateArguments(BaseModel, frozen=True):
    command: Literal["validate"]
    root: Path
    manifest: Path
    audit: Path

    def run(self) -> int:
        validate(self.root, self.manifest, self.audit)
        print("validated Item 6 frozen configuration and audit")
        return 0


_ARGUMENTS_ADAPTER: TypeAdapter[_CaptureArguments | _ValidateArguments] = TypeAdapter(
    _CaptureArguments | _ValidateArguments
)


def main() -> int:
    """Run capture or validation."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    capture_parser = subparsers.add_parser("capture")
    _ = capture_parser.add_argument("--instance", type=Path, required=True)
    _ = capture_parser.add_argument("--output", type=Path, required=True)
    validate_parser = subparsers.add_parser("validate")
    _ = validate_parser.add_argument("--root", type=Path, required=True)
    _ = validate_parser.add_argument("--manifest", type=Path, required=True)
    _ = validate_parser.add_argument("--audit", type=Path, required=True)
    arguments = _ARGUMENTS_ADAPTER.validate_python(vars(parser.parse_args()), strict=True)
    return arguments.run()


if __name__ == "__main__":
    raise SystemExit(main())
