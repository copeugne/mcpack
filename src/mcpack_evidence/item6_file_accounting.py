# ruff: noqa: EM101, EM102, TRY003
"""Validate the stable scope rationale for Item 6 file accounting."""

from __future__ import annotations

from typing import Final, TypedDict


class Classification(TypedDict):
    """One exhaustive frozen-file classification with its fixed scope rule."""

    classification: str
    rationale: str
    files: list[str]


RATIONALES: Final = {
    "audited": (
        "Audited paths control or directly inform Item 6 named systems, settings, or findings."
    ),
    "out-of-scope": (
        "Out-of-scope paths are preserved and identity-checked but do not control required "
        "Item 6 systems."
    ),
}


def validate_file_accounting(
    expected: set[str], covered: set[str], classifications: list[Classification]
) -> None:
    """Require an exhaustive, exact, and rationale-bound classification partition."""
    accounted: set[str] = set()
    for classification in classifications:
        label = classification["classification"]
        if classification["rationale"] != RATIONALES.get(label):
            raise ValueError("invalid file-accounting rationale")
        for relative in classification["files"]:
            if relative in accounted:
                raise ValueError(f"file is classified more than once: {relative}")
            accounted.add(relative)
    if accounted != expected:
        missing = sorted(expected - accounted)
        extra = sorted(accounted - expected)
        raise ValueError(
            f"file accounting does not match manifest: missing={missing}, extra={extra}"
        )
    audited = {
        relative
        for classification in classifications
        if classification["classification"] == "audited"
        for relative in classification["files"]
    }
    if audited != covered:
        raise ValueError("audited file accounting does not match cited audit evidence")
