# Item 4 — Controlled Test Environment Closure

**Status:** `COMPLETE`
**Configuration:** `test-environment-v0.1`

## Exit-gate result

Any current experiment can be regenerated from versioned inputs or rolled back to a hash-verified stopped-world archive. The pristine baseline, engineering experiment, generated seed worlds, and restore-validation tree occupy separate paths. No production instance exists.

## Seed suite

| Role | Seed | Acceptance evidence | Result |
|---|---:|---|---|
| Ordinary | `42` | Plains 520 blocks; forest 385; jagged peaks 2,648 | Pass |
| Mountainous | `6671238423019257953` | Jagged peaks at spawn, Y=242 | Pass |
| Ocean-heavy | `95920844204830198` | Cold ocean 101; deep cold ocean 226; forest 968 | Pass |
| Biome-diverse | `-3503646078644842058` | Six queried families within 1,100; cold/wet/ocean contrasts within 2,500 | Pass |

Every world independently booted Minecraft 1.21.1 + NeoForge 21.1.249 with zero third-party mods, ran serial biome queries, completed `save-all flush`, and stopped cleanly. The parser's results are corroborated against retained full debug logs. Two earlier harness defects—blocking timeouts and unbound reader state—were detected and corrected; no result from those runs is accepted.

## Preserved initial worlds

| Role | Files | Uncompressed bytes | Archive SHA-256 |
|---|---:|---:|---|
| Ordinary | 17 | 4,263,957 | `00b32b91d854a5ad46c3acb839236daf834f55be287a3f5a38e3c2807b71d7ea` |
| Mountainous | 17 | 4,444,172 | `70165e05f808ce26ff5800e235a4a44231ef03036a1597b173e0cf2cf4814779` |
| Ocean-heavy | 21 | 3,249,573 | `383e7f25028262ae08c738bd8900cf07a7063f044582c7143341bcad05f7149f` |
| Biome-diverse | 14 | 4,010,024 | `535624fc8e84fe62752f65300db3b604a94c7aa3a3c2f450c3c1d15fc3a8ef92` |

Archives remain outside Git; JSON receipts retain the archive hash and each included file's path, size, and SHA-256.

## Backup and restore proof

- Active-world lock simulation: backup refused with a non-zero exit.
- Ordinary seed archive SHA-256: verified before extraction.
- Restored file manifest: exact, 17 files and 4,263,957 bytes.
- Restored-world boot: `Done (1.440s)`.
- Reported restored seed: `42`.
- Restored world: saved, flushed, and stopped cleanly.
- Restore debug-log SHA-256: `0f3521a348aa6da6552d6f60b78776cccfdb304d70b6bf908039fa81a7ab3780`.

## Versioning and source control

The naming contract, regeneration procedure, version-controlled input policy, and backup rules are recorded in `test-environment/README.md`. Git is initialized on `main`; work is committed in atomic logical units. Configs are versioned, and datapack/spawn-rule/loot/worldgen override inventories are explicitly empty rather than assumed absent.

## Deferred production-only variables

Backup frequency, retention, remote replication, recovery-point objective, recovery-time objective, hosting hardware, and production operations remain logged unknowns. They do not block the isolated Item 4 exit gate but must be resolved before production validation.

