"""Apply FML physical-side and dependency range semantics for Item 3."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Literal

from mcpack_evidence.item3_compatibility_models import DependencyCheck, ProvidedMod, RangeCheck

if TYPE_CHECKING:
    from mcpack_evidence.item3_jar_models import DependencyDeclaration

type RangeOracle = Callable[[str, str], str]
type DependencyStatus = Literal[
    "pass",
    "missing_required",
    "version_mismatch",
    "incompatible_present",
    "discouraged_present",
    "optional_absent",
    "ignored_physical_side",
    "orphan_owner_ignored",
    "unresolved",
]
type RangeResult = Literal["pass", "fail", "invalid", "missing_oracle_result"]
_BUILT_INS = {"minecraft": "1.21.1", "neoforge": "21.1.249"}


def evaluate_dependency(
    dependency: DependencyDeclaration,
    own_mods: tuple[ProvidedMod, ...],
    providers: dict[str, list[ProvidedMod]],
    oracle: RangeOracle,
) -> DependencyCheck:
    """Evaluate one active dependency exactly as it applies on a dedicated server."""
    if dependency.owner_mod_id not in {mod.mod_id for mod in own_mods}:
        return _result(dependency, "orphan_owner_ignored")
    if not applies_to_server(dependency.side):
        return _result(dependency, "ignored_physical_side")
    if dependency.mod_id in _BUILT_INS:
        checks = tuple(
            target_range_check(dependency.mod_id, _BUILT_INS[dependency.mod_id], value, oracle)
            for value in dependency.version_ranges
        )
        return _result(dependency, _present_status(dependency.kind, checks), checks=checks)
    matches = providers.get(dependency.mod_id, [])
    if not matches:
        status: DependencyStatus = (
            "missing_required" if dependency.kind.casefold() == "required" else "optional_absent"
        )
        return _result(dependency, status)
    checks = tuple(
        range_check(dependency.mod_id, provider.version, declared_range, oracle)
        for provider in matches
        for declared_range in dependency.version_ranges
    )
    return _result(dependency, _present_status(dependency.kind, checks), matches, checks)


def target_range_check(
    subject: str,
    version: str,
    declared_range: str,
    oracle: RangeOracle,
) -> RangeCheck:
    """Apply the exact 1.21.1 FML support-matrix fallback after a direct failure."""
    direct = range_check(subject, version, declared_range, oracle)
    fallback = {"minecraft": "1.21", "neoforge": "21.0.166"}.get(subject)
    if direct.result != "fail" or fallback is None:
        return direct
    if oracle(fallback, declared_range) == "pass":
        return direct.model_copy(update={"result": "pass", "fallback_version": fallback})
    return direct


def range_check(
    subject: str,
    version: str,
    declared_range: str,
    oracle: RangeOracle,
) -> RangeCheck:
    """Ask the frozen external Maven oracle to evaluate one version-range pair."""
    raw_result = oracle(version, declared_range)
    allowed: tuple[RangeResult, ...] = ("pass", "fail", "invalid", "missing_oracle_result")
    if raw_result not in allowed:
        message = f"unsupported oracle result: {raw_result}"
        raise ValueError(message)
    result = raw_result
    return RangeCheck(
        subject=subject,
        installed_version=version,
        declared_range=declared_range,
        result=result,
    )


def applies_to_server(side: str) -> bool:
    """Return whether an FML dependency applies to the dedicated-server physical side."""
    return side.casefold() not in {"client", "client_only"}


def _present_status(kind: str, checks: tuple[RangeCheck, ...]) -> DependencyStatus:
    if any(check.result in {"invalid", "missing_oracle_result"} for check in checks):
        return "unresolved"
    matched = any(check.result == "pass" for check in checks) or not checks
    if kind.casefold() in {"incompatible", "conflicting"}:
        return "incompatible_present" if matched else "pass"
    if kind.casefold() == "discouraged":
        return "discouraged_present" if matched else "pass"
    return "pass" if matched else "version_mismatch"


def _result(
    dependency: DependencyDeclaration,
    status: DependencyStatus,
    providers: list[ProvidedMod] | tuple[()] = (),
    checks: tuple[RangeCheck, ...] = (),
) -> DependencyCheck:
    return DependencyCheck(
        owner_mod_id=dependency.owner_mod_id,
        dependency_mod_id=dependency.mod_id,
        kind=dependency.kind,
        side=dependency.side,
        status=status,
        provider_candidates=tuple(row.provider_candidate for row in providers),
        range_checks=checks,
    )
