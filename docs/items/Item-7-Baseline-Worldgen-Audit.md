# Item 7 Baseline Worldgen Interaction Audit

**Acceptance status:** `PASS`
**Delivery status:** awaiting pull request review and merge
**Protocol:** `item7-worldgen-audit-v1`
**Frozen stack:** 136 retained JARs under Minecraft 1.21.1, NeoForge 21.1.249, and Temurin 21.0.12.1+1-LTS

## Decision

Item 7's local exit gate passes. The retained stack was exercised in actual fresh worlds under the exact frozen Item 6 configuration, every required provider label and anomaly class has an evidence-backed disposition, the raw evidence is durably published and restore-tested, and the deterministic completion validator returns `PASS`.

This is not a clean-worldgen claim. Independent fresh runs diverged semantically outside the central End, Better Caves emitted a confirmed generation failure, two YUNG components remain unobserved because canonical structure identifiers are unresolved, and most warning signatures remain `UNKNOWN`. These findings are carried forward to Item 8 and later gates. No Item 6 configuration was tuned.

## Bound identity and sampling geometry

The protocol binds the following inputs exactly:

- retained manifest count 136, SHA-256 `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`;
- frozen configuration manifest SHA-256 `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f`;
- configuration audit SHA-256 `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd`;
- seed-suite SHA-256 `de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae`;
- ordinary seed `42`, mountainous seed `6671238423019257953`, ocean-heavy seed `95920844204830198`, and biome-diverse seed `-3503646078644842058`.

Run A and Run B each used fresh materializations for all four seeds. Each run generated and inspected four fixed selections: 3,969 Overworld chunks, 961 Nether chunks, 961 central End chunks, and 961 outer End chunks. This is 6,852 selected chunks per seed run, 27,408 per run ID, and 54,816 selected chunks across the eight accepted seed runs. Every selected chunk was present exactly once at `minecraft:full` status. Spawn and transport extras were inventoried separately rather than counted as selected observations.

The separately declared Chunky 1.4.23 JAR was used only as a generation instrument. The retained-stack control used exactly the 136 retained JARs and vanilla `forceload`, with no Chunky files.

## Provider coverage

The audit covered every provider label required by `SPECS.md`: Tectonic, Terralith, Biomes O' Plenty, Regions Unexplored, TerraBlender, Lithostitched, BetterEnd, YUNG, WDA, IDAS, Integrated structures, Moog, Explorify, Explorations, Repurposed Structures, CTOV, and Towns & Towers.

The catalog contains 37 exact retained components. Final dispositions are:

| Disposition | Components | Meaning |
|---|---:|---|
| Directly observed | 23 | Saved decoded chunks contain provider-owned biomes or structure starts. |
| Targeted observed | 4 | Two independent targeted runs each saved the same requested structure start. |
| Observed generation failure | 1 | Better Caves logged an `AquiferContext` failure and warned that Liquid Regions may not generate correctly. |
| Indirectly observed | 7 | Runtime evidence proves a loaded or executed consumer path, but saved output cannot be attributed directly. |
| Not observed with explicit limit | 2 | YUNG's Bridges and YUNG's Extras lack resolved canonical structure identifiers and remain Item 8 follow-ups. |

The four targeted structures were Better Desert Temples, Better Strongholds, Better Witch Huts, and Integrated Stronghold. Targeted observation proves generation at the located coordinates, not frequency.

## Interaction and anomaly inspection

Sixteen Run A analysis reports cover all four seeds and all four selections. Each report contains one row for every required anomaly class, for 192 rows total. The analysis records denominators, candidates, method, status, and limitations. Fragmented and tiny biomes, terrain transitions, structure overlaps, and village overlaps were measured directly. Biome sampling uses the decoder's highest occupied Y directly. Floating placement is always method-limited because post-placement `WORLD_SURFACE` includes the structure and cannot prove an air gap below it. Buried, cliff, underwater, and terrain-modification checks become method-limited where complete terrain or footprint inputs are unavailable. Failed placement is method-limited because invalid starts omitted by the decoder cannot be treated as a complete absence.

The hash-bound packaged restriction audit inspected all 762 structure definitions supplied by the exact 37 Item 7 provider components plus frozen Minecraft and NeoForge data. It resolved 757 definitions and found five impossible restrictions. Dungeons Arise's unplaced mining system and Terralith's unplaced underground witch hut deliberately use empty tags. Three IDAS lumber-camp compatibility variants reference missing biome tags while remaining members of the active `idas:idas_small` placement set. Those three findings are carried into Item 8; the Item 7 inspection subitem is resolved rather than reported as unknown.

Candidate counts are deterministic geometric or registry signals, not automatic gameplay defects. The 128 final offline captures provide elevation, biome, structure-overlay, and cross-section views for every seed, selection, and run. Two independent review lanes passed artifact identity, legends, orientation, scale, axes, units, limitations, clipping, and plot padding. The renders are derived inspection views, not block-accurate client screenshots.

## Repeatability and control result

Run A and Run B are not semantically equal. All central End selections match. Overworld, Nether, and outer End selections contain genuine heightmap, biome-section, or structure-start differences depending on seed and dimension. Exact inputs, selected coordinates, lifecycle commands, configuration semantics, decoder ordering, and transport-only fields were checked and do not explain the divergence.

The causal provider is `UNKNOWN`. An order-sensitive worldgen interaction is plausible but unconfirmed. Changing C2ME or another frozen setting would be a tuning experiment and was not permitted inside Item 7.

The retained-136 control compared 81 exact Overworld chunks against the accepted pilot. It found two heightmap mismatches and no biome or structure-start mismatches. Because the full retained stack itself demonstrated semantic nondeterminism, the control result is `not_attributable_due_to_measured_stack_nondeterminism`, not proof that Chunky changed terrain.

## Warning evidence

The accepted warning audit preserves 1,222 exact signatures and 14,003 occurrences: 10,095 warning occurrences and 3,908 error occurrences. The downstream disposition records:

- 39 confirmed generation-failure signatures with 50 occurrences;
- 11 performance signatures with 11 occurrences;
- 6 follow-up signatures with 141 occurrences;
- 1,166 unresolved signatures with 13,801 occurrences.

Unresolved entries remain `UNKNOWN`. The audit does not convert startup success into compatibility proof and does not discard duplicate, noisy, or unattributed messages.

## Durable evidence and restoration

The final raw evidence is split into four immutable release assets under tag `item-7-raw-evidence-2026-09-04-r7`, bound to corrected source revision `ca646c19ad772bd6de6a47f4dcb0fc5dc4b5cbfc`:

| Asset | Files | Raw bytes | Archive bytes | Archive SHA-256 |
|---|---:|---:|---:|---|
| Core | 4,618 | 2,515,785,938 | 243,943,142 | `2229673778123d8b7737048610d9c171aea9b49900724acc0f35ac48eed25773` |
| Run A worlds | 249 | 484,774,742 | 291,011,199 | `575b8644bb888e2f2c09311f0ba3ac063ea00eda1d51159e0038218a28d96fa7` |
| Run B worlds | 250 | 484,038,098 | 289,949,293 | `3a82829fa159323ec1844d6f98fdc9ab6b25feab78d15c1b268d2a2692c268ff` |
| Auxiliary worlds | 217 | 165,166,012 | 48,648,807 | `d865320a9b1d2b44e59eb7d854fa499309746dc71a04b6b8caa46ede2a0c5a25` |

All four archives were restored into absent targets, checked file by file, downloaded twice from the published GitHub release, and rehashed. The committed publication receipt and completion validator bind the release URL, tag, source revision, asset names, sizes, hashes, manifests, restore receipts, and verification tool. The independently constructed world archive inventory also binds all 716 raw Run A, Run B, and auxiliary world files to those manifests. JARs, Minecraft and NeoForge binaries, credentials, `session.lock`, player data, caches, and symlinks are excluded.

The first release, r2, r3, and r4 remain preserved as historical evidence. The first procedure did not hold Java-compatible world locks and used hardlinks. The r2 procedure added locks and independent copies, but later review proved that its reusable staging and archive implementation still had pathname replacement gaps. r3 proved corrected creation custody, but the later GitHub review found invalid floating-placement and biome-height semantics plus incomplete raw-world binding. r4 preserves r3 outputs as explicitly superseded data, regenerates all 32 analyses and galleries plus all 128 captures with the corrected code, and adds the independent world archive inventory. The exact-SHA review at `5a5623fbe161c3ab1874c8184b8f9f1d0418c9cd` then proved that restore target and receipt publication remained pathname-based. Tags r5 and r6 preserve unpublished failed attempts while that defect and a real descriptor-scan offset defect were corrected.

Reviews of revisions `8c7e7b8bb5db79d826b78cab5a678605a8b5fc23` and `438260f40fd0d50ff5f087a2b8aac028d5a39927` found remaining source, output, hardlink, special-file, and repository-binding defects. Commits `fdd99d9`, `c625d6e`, `f57503d`, and `4503d64` correct those boundaries and the vacuous mutation tests with focused regression coverage.

The r7 archives were rebuilt from the hash-verified r4 restore with the final descriptor-bound implementation. Restore writes into an unpublished tree through pinned descriptors, rehashes its complete inventory, publishes without replacement, and emits a receipt from a pinned directory only while the published target still names the verified inode. All four r7 archives restored into absent targets. Two independent downloads with the tracked repository-bound verifier matched every committed size and SHA-256. The canonical completion rebuild uses the r7 restored core, not the older mutable construction tree. Rejected review records remain under `evidence/item-7/review/`; a fresh exact-SHA review remains required before delivery.

## Reproduction

All acceptance-relevant implementation, CLIs, and tests are tracked under `src/mcpack_evidence/`, `tools/`, and `tests/item7/`. The protocol and committed receipts are under `evidence/item-7/`. The exact runtime commands and their outputs are retained in the raw archives.

The final local checks are:

```bash
uv run pytest -q tests/item7
uv run ruff format --check src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
uv run ruff check src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
uv run basedpyright src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
bash -n tools/stage_item7_raw_evidence.sh
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r7 evidence/item-7/archive/r7 evidence/item-7/archive/r7/publication.json /tmp/item7-release-verify-r7
```

The Python quality commands are intentionally scoped to Item 7. They do not claim that unrelated reconstructed later-item tools are clean, and Item 11 tooling remains outside this gate until the required Item 2 through Item 10 cross-item audit passes.

After restoring all four r7 assets, run the tracked `tools/build_item7_completion.py` CLI with `--raw-root` and `--visual-manifest` under the restored r7 core, `--world-archive-inventory evidence/item-7/world-archive-inventory.json`, and the r7 archive manifests, restore receipts, and publication receipt. The remaining protocol, provider, biome-restriction, repeat, warning, and control inputs are the matching tracked or restored-core paths. The exact accepted invocation is recorded in `evidence/item-7/review/candidate-r7-validation.md`. It returns `PASS`, records 125 artifact identities, and must not use the older mutable `/tmp/mcpack-item7-raw-20260904` tree.

## Evidence index

- `evidence/item-7/protocol/worldgen-audit-v1.json`
- `evidence/item-7/provider-catalog.json`
- `evidence/item-7/biome-restriction-audit.json`
- `evidence/item-7/world-archive-inventory.json`
- `evidence/item-7/visual/integrity-review.json`
- `evidence/item-7/visual/fidelity-review.json`
- `evidence/item-7/visual/rejected-attempts.json`
- `evidence/item-7/archive/r7/`
- `evidence/item-7/review/`
- `evidence/item-7/completion.json`
- GitHub release `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r7`

## Superseded historical control

The former zero-mod `terrain-control-v0.1` report was reconstructed prose whose raw samples, verification file, and probe tool were lost. Its reported 200 exact repeated samples remain historical context only. This retained-stack audit replaces it as Item 7 acceptance evidence.

## Exit decision

The local Item 7 exit gate passes, with the limitations and downstream actions above preserved. Item 7 reaches repository-level `COMPLETE` only after this branch receives clean exact-SHA review and merges into `main`. Item 8 must then begin from that verified merged ref and must resolve canonical family identities without double-counting aliases, pieces, pools, or templates.
