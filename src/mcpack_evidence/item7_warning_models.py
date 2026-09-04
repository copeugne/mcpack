"""Strict Item 7 warning-audit evidence models."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import ClassVar, Literal, override

from pydantic import BaseModel, ConfigDict


class Disposition(StrEnum):
    """Conservative handling state for one observed signature."""

    REQUIRES_FOLLOW_UP = "requires_follow_up"
    UNTRIAGED = "untriaged"


class ConsumerStatus(StrEnum):
    """Whether the runtime line itself identifies the warning consumer."""

    IDENTIFIED = "identified"
    UNRESOLVED = "unresolved"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True, slots=True)
class WarningAuditError(Exception):
    """A warning log cannot be read or emitted without losing evidence."""

    detail: str

    @override
    def __str__(self) -> str:
        """Render the evidence-bound failure detail."""
        return self.detail


class _StrictModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)


class EvidenceLine(_StrictModel):
    """The deterministic first raw line supporting a signature."""

    path: str
    line: int
    text: str


class WarningSignature(_StrictModel):
    """One deduplicated warning or error signature with preserved uncertainty."""

    signature_id: str
    severity: Literal["WARN", "ERROR"]
    occurrences: int
    first_evidence: EvidenceLine
    provider_mod_tokens: tuple[str, ...]
    disposition: Disposition
    consumer_status: ConsumerStatus


class WarningAudit(_StrictModel):
    """Strict machine-readable audit of warning and error log entries."""

    schema_version: Literal["item7-warning-audit-v1"]
    input_logs: tuple[str, ...]
    signatures: tuple[WarningSignature, ...]
    warning_occurrences: int
    error_occurrences: int
    untriaged_signatures: int


__all__ = (
    "ConsumerStatus",
    "Disposition",
    "EvidenceLine",
    "WarningAudit",
    "WarningAuditError",
    "WarningSignature",
)
