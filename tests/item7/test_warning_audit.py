from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tools.audit_item7_warnings import run

from mcpack_evidence.item7_warnings import (
    ConsumerStatus,
    Disposition,
    WarningAudit,
    WarningAuditError,
    audit_logs,
)

if TYPE_CHECKING:
    from pathlib import Path


def _write(path: Path, *lines: str) -> None:
    _ = path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _line(severity: str, logger: str, message: str, *, time: str = "07:10:40.829") -> str:
    return f"[04Sep2026 {time}] [c2me-worker-3/{severity}] [{logger}/]: {message}"


def test_audit_deduplicates_signatures_with_counts_and_stable_first_lines(
    tmp_path: Path,
) -> None:
    latest = tmp_path / "a-latest.log"
    console = tmp_path / "z-console.log"
    cabin = (
        "Integrated API: Empty or nonexistent pool: "
        "integrated_villages:cabin_village/villager_random which is being called from not a "
        "SinglePoolElement class"
    )
    yung_message = (
        "Discarding @Unique public method getEnhancedJunctionIterator in "
        "yungsapi.mixins.json:BeardifierMixin from mod yungsapi because it already exists in "
        "net.minecraft.world.level.levelgen.Beardifier"
    )
    moog_message = (
        "Discarding @Unique public method getEnhancedPieceIterator in "
        "moogs_structures-common.mixins.json:terrainadaptation.BeardifierMixin from mod "
        "moogs_structures because it already exists in "
        "net.minecraft.world.level.levelgen.Beardifier"
    )
    wover_conflict = (
        "Method overwrite conflict for getChunk in "
        "wover.surface.mixins.common.json:SurfaceRulesContextAccessor from mod wover, previously "
        "written by dev.worldgen.lithostitched.mixin.common.SurfaceRulesContextMixin. "
        "Skipping method."
    )
    bclib_conflict = wover_conflict.replace(
        "wover.surface.mixins.common.json", "bclib.mixins.common.json"
    ).replace("from mod wover", "from mod bclib")
    _write(
        latest,
        _line("WARN", "com.craisinlord.integrated_api.IntegratedAPI", cabin),
        _line(
            "WARN",
            "mixin",
            yung_message,
        ),
        _line("WARN", "mixin", moog_message),
        _line("WARN", "mixin", wover_conflict),
        _line("WARN", "example", "Unrecognized pilot warning"),
    )
    _write(
        console,
        _line("WARN", "co.cr.in.IntegratedAPI", cabin, time="07:10:41.003"),
        _line("WARN", "co.cr.in.IntegratedAPI", cabin, time="07:10:41.004"),
        _line("WARN", "mixin", bclib_conflict, time="07:10:41.004"),
        _line("WARN", "example", "Unrecognized pilot warning", time="07:10:41.005"),
    )

    audit = audit_logs((console, latest), evidence_root=tmp_path)
    by_id = {signature.signature_id: signature for signature in audit.signatures}

    assert audit.schema_version == "item7-warning-audit-v1"
    assert audit.input_logs == (latest.name, console.name)
    cabin_signature = by_id["integrated-villages-empty-cabin-pool"]
    assert cabin_signature.occurrences == 3
    assert cabin_signature.first_evidence.path == latest.name
    assert cabin_signature.first_evidence.line == 1
    assert cabin_signature.provider_mod_tokens == ("integrated_api", "integrated_villages")
    yung = by_id["yung-beardifier-unique-method-discard"]
    assert yung.occurrences == 1
    assert yung.provider_mod_tokens == ("yungsapi",)
    assert by_id["moog-beardifier-unique-method-discard"].provider_mod_tokens == (
        "moogs_structures",
    )
    surface = by_id["surface-rules-overwrite-conflict"]
    assert surface.occurrences == 2
    assert surface.provider_mod_tokens == ("bclib", "lithostitched", "wover")
    untriaged = [item for item in audit.signatures if item.disposition is Disposition.UNTRIAGED]
    assert len(untriaged) == 1
    assert sum(item.occurrences for item in untriaged) == 2
    assert audit.warning_occurrences == 9
    assert audit.error_occurrences == 0


def test_audit_preserves_unresolved_ownership_and_never_launders_unknowns(
    tmp_path: Path,
) -> None:
    log = tmp_path / "latest.log"
    basalt = "Couldn't find template pool reference: minecraft:basalt_chambers/chambers"
    save_hook_message = (
        "Certain optimizations may be disabled because ChunkDataEvent.Save is used by: "
        "[@SubscribeEvent: class dev.architectury.event.forge.EventHandlerImplCommon "
        "eventChunkDataEvent(Lnet/neoforged/neoforge/event/level/ChunkDataEvent$Save;)V]"
    )
    _write(
        log,
        _line("WARN", "lithostitched", f"{basalt} (Jigsaw block location: 160, 15, -141)"),
        _line("WARN", "lithostitched", f"{basalt} (Jigsaw block location: 143, 15, -138)"),
        _line(
            "WARN",
            "C2ME HookCompatibility",
            save_hook_message,
        ),
        _line("ERROR", "unknown-provider", "A new unexplained generation failure"),
    )

    audit = audit_logs((log,), evidence_root=tmp_path)
    by_id = {signature.signature_id: signature for signature in audit.signatures}

    missing_pool = by_id["basalt-chambers-missing-pool"]
    assert missing_pool.occurrences == 2
    assert missing_pool.disposition is Disposition.REQUIRES_FOLLOW_UP
    assert missing_pool.consumer_status is ConsumerStatus.UNRESOLVED
    assert missing_pool.provider_mod_tokens == ("lithostitched", "minecraft")
    save_hook = by_id["c2me-chunk-save-hook"]
    assert save_hook.disposition is Disposition.REQUIRES_FOLLOW_UP
    assert save_hook.consumer_status is ConsumerStatus.UNRESOLVED
    assert save_hook.provider_mod_tokens == ("architectury", "c2me")
    assert "chunky" not in save_hook.provider_mod_tokens
    unknown = next(item for item in audit.signatures if item.severity == "ERROR")
    assert unknown.disposition is Disposition.UNTRIAGED
    assert unknown.consumer_status is ConsumerStatus.UNRESOLVED
    assert audit.untriaged_signatures == 1


def test_cli_writes_strict_json_atomically_and_preserves_existing_output_on_failure(
    tmp_path: Path,
) -> None:
    log = tmp_path / "latest.log"
    output = tmp_path / "audit.json"
    _write(log, _line("WARN", "unknown-provider", "Unexplained warning"))
    _ = output.write_text("sentinel\n", encoding="utf-8")

    assert run(("--root", tmp_path.as_posix(), log.as_posix(), "--output", output.as_posix())) == 0
    document = WarningAudit.model_validate_json(output.read_bytes())
    assert document.schema_version == "item7-warning-audit-v1"
    assert document.untriaged_signatures == 1

    with pytest.raises(WarningAuditError, match="cannot read warning log"):
        _ = run(
            (
                "--root",
                tmp_path.as_posix(),
                (tmp_path / "missing.log").as_posix(),
                "--output",
                output.as_posix(),
            )
        )
    assert WarningAudit.model_validate_json(output.read_bytes()) == document


def test_run_a_unknown_worldgen_events_remain_counted_and_untriaged(tmp_path: Path) -> None:
    log = tmp_path / "run-a-latest.log"
    invalid_air = "Tried to load invalid item: 'Item must not be minecraft:air'"
    _write(
        log,
        _line("ERROR", "net.minecraft.world.item.ItemStack", invalid_air),
        _line("ERROR", "net.minecraft.world.item.ItemStack", invalid_air),
        _line(
            "WARN",
            "net.minecraft.world.entity.ai.attributes.AttributeMap",
            "Ignoring unknown attribute 'forge:step_height_addition'",
        ),
        _line(
            "WARN",
            "net.minecraft.world.entity.ai.attributes.AttributeMap",
            "Ignoring unknown attribute 'forge:entity_gravity'",
        ),
        _line(
            "WARN",
            "net.minecraft.world.entity.EntityType",
            "Skipping Entity with id guardvillagers:guard",
        ),
    )

    audit = audit_logs((log,), evidence_root=tmp_path)
    untriaged = [item for item in audit.signatures if item.disposition is Disposition.UNTRIAGED]
    invalid = next(item for item in untriaged if item.severity == "ERROR")

    assert len(untriaged) == 4
    assert invalid.occurrences == 2
    assert invalid.first_evidence.line == 1
    assert invalid.provider_mod_tokens == ("minecraft",)
    assert {token for item in untriaged for token in item.provider_mod_tokens} >= {
        "forge",
        "guardvillagers",
        "minecraft",
    }


def test_audit_records_paths_relative_to_declared_evidence_root(tmp_path: Path) -> None:
    run = tmp_path / "run-a/ordinary"
    run.mkdir(parents=True)
    log = run / "minecraft-latest.log"
    _write(log, _line("WARN", "example", "Relative evidence path"))

    audit = audit_logs((log,), evidence_root=tmp_path)

    assert audit.input_logs == ("run-a/ordinary/minecraft-latest.log",)
    assert audit.signatures[0].first_evidence.path == "run-a/ordinary/minecraft-latest.log"
