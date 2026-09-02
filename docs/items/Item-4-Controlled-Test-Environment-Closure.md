# Item 4 — Controlled Test Environment Closure

**Status:** `COMPLETE`
**Configuration:** `test-environment-v0.1`

## Exit-gate result

Any Item 4 experiment can be recreated from versioned inputs or rolled back into a new target from a hash-verified stopped-world archive. Runtime work is isolated under `instances/item4`; no production instance was present or read. The environment uses Minecraft 1.21.1, NeoForge 21.1.249, Temurin 21.0.12.1+1, the exact 136-candidate retained manifest, and the Item 2 baseline configuration.

## Deterministic seed controls

| Role | Seed | Full retained-stack lifecycle |
|---|---:|---|
| Ordinary | `42` | Ready in 125.098s; flush and clean stop passed |
| Mountainous | `6671238423019257953` | Ready, flush, and clean stop passed in 406.918s |
| Ocean-heavy | `95920844204830198` | Ready, flush, and clean stop passed in 338.181s |
| Biome-diverse | `-3503646078644842058` | Ready, flush, and clean stop passed in 345.989s |

All four controls were independently materialized with exactly 136 hash-verified retained artifacts. Item 4 fixes their identities and proves lifecycle isolation. Item 7 remains responsible for empirical terrain, biome, structure, and cross-mod world-generation inspection.

## Backup and restore proof

The ordinary world was flushed and stopped before backup. Its deterministic archive contains 58 files, is 1,190,041 bytes, and has SHA-256 `2df51369e1c31407f5eb91f0db04f39c631ee0df712235831c2e2853dbe4a772`. Restore verified that hash before safe extraction into an absent target. The restored world contained the same 58 recorded files, reached readiness in 62.224 seconds, flushed, and stopped cleanly.

The archive remains in the ignored backup store; `evidence/item-4/ordinary-backup-receipt.json` records every world-relative file, size, and SHA-256. The restore receipt and compressed runtime log are committed.

## Failure preservation

An initial mountainous run used a fixed five-minute delayed command pipe. The server reached readiness but the unchanged 60-second watchdog terminated a subsequent tick before the delayed flush arrived. The log and crash report are retained rather than discarded. This was classified as a procedural harness defect: the control was recreated from scratch and rerun with a readiness-driven harness that immediately flushed and stopped, which passed. No watchdog setting or generated configuration was altered.

## Versioning and rollback

`test-environment/README.md` defines configuration and experiment branch naming, clean regeneration, backup, restore, and rollback. Materialization removes any world copied from the pristine reconstruction before applying the selected seed. Backup holds a Minecraft-compatible POSIX record lock across both archive creation and receipt hashing. The lifecycle tools refuse existing targets, verify retained artifact identities, use deterministic archives, verify archive hashes before extraction, and reject unsafe members. Config inputs are versioned through Item 2 evidence; project datapack, spawn-rule, loot-table, and worldgen-override inventories are explicitly empty. Generated mod configs remain untuned inputs for Item 6.

## Known limitations carried forward

This gate proves deterministic setup, isolation, initial world boot, backup integrity, and restored-world boot. It does not approve terrain, structures, gameplay, client join, or performance. Network-dependent optional diagnostics remained unavailable to the Java runtime and are not treated as compatibility conclusions.

## Exit-gate assessment

`SPECS.md` Item 4 passes: the dedicated test server is separate, the validated baseline is cloned reproducibly, four deterministic seed controls are materialized and boot-validated, versioning and clean regeneration are documented, relevant project inputs are version-controlled, and an actual hash-verified backup/restore was proven by a restored-world boot. Item 5 is now dependency-eligible. Item 11 remains unauthorized.
