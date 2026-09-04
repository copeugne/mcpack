# Item 6: Retained-stack generated configuration audit

## Exit decision

**PASS.** The exact 136-JAR retained server stack was reconstructed under Minecraft 1.21.1, NeoForge 21.1.249, and Eclipse Temurin 21.0.12.1+1-LTS. A new ordinary seed-42 instance reached readiness, completed `save-all flush`, and stopped cleanly. No setting was tuned. The post-shutdown configuration tree is frozen losslessly in `evidence/item-6/frozen/`; the sorted 228-file manifest binds every relative path, byte size, SHA-256, and generation stage.

The capture distinguishes 4 installation/materialization files, 223 first-startup files, and 1 world-creation server config. No file first appeared only during shutdown. The post-shutdown state is the effective baseline. The validator independently verifies exact tree equality, every file identity, report-to-manifest references, literal setting evidence, the audit's manifest identity, and one accounting classification for each of the 228 manifest paths. The 35 audited paths are exactly the union cited by systems, settings, and findings. The remaining 193 paths are explicitly out of scope.

## Reconstruction and capture boundary

The run reacquired and hash-verified all platform artifacts and all 190 audited candidate artifacts, materialized only the 136 retained candidates, and removed the copied Item 2 world before applying seed 42. The NeoForge installer required the environment HTTP proxy and an operational-only Java trust store; neither was committed. The committed lifecycle receipt proves readiness, explicit flush confirmation, clean stop, and return code zero. The compressed log preserves generation diagnostics.

The frozen tree contains `config/`, `defaultconfigs/`, `world/serverconfig` (normalized to `world-serverconfig/` in the evidence root), and `server.properties`. Candidate JARs, binaries, the generated world, caches, and the operational trust store remain excluded.

## Configuration findings

### Density and structure placement

* **Sparse Structures is the primary explicit low-density control.** Its generated global `spreadFactor` is 2, so structure placements are made rarer. The generated mansion override is also factor 2. The precise way global and per-structure factors compose must be confirmed from runtime density evidence rather than guessed.
* **Structure Essentials exposes a second global placement control**, but `spacingSeparationModifier` is neutral at 1.0. Its 32-block minimum-distance feature is disabled, as are automatic biome compatibility and overlap logging. Fast lookup is enabled and search radii differ from vanilla as documented in the generated file.
* **Structure Layout Optimizer** retains its seed-parity-preserving default: template-pool list deduplication is false.
* **Cristel Lib emits provider placement and toggle files.** WDA major/minor sets use 50/45 and 45/40 spacing/separation before any global Sparse Structures effect, and all listed WDA families are enabled. Equivalent preserved files cover Seven Seas, IDAS, Integrated structures, Explorations/Explorify, four Moog namespaces, Repurposed Structures, and YUNG providers. The machine-readable audit cites each audited YUNG placement scalar and enabled toggle without falsely treating aliases or pieces as Item 8 families.
* **Explicit replacements exist.** Six YUNG generated defaults disable vanilla desert pyramids, Nether fortresses, jungle temples, mineshafts, ocean monuments, and witch huts. IDAS also disables the vanilla desert pyramid, so that replacement is duplicated in the generated configuration. Integrated Villages disables vanilla villages. These are disabled vanilla sets caused by replacements, not missing generation.

### YUNG control surfaces

The YUNG structure inventory includes the Cristel Lib placement and toggle files for Better Desert Temples. The placement evidence records every spacing and separation value. The toggle evidence records every enabled structure leaf. Sparse Structures remains a separate global factor that may interact with these enabled placements.

### Villages, loot, mobs, difficulty, and performance

* Village ownership is crowded: CTOV, Towns & Towers, Better Village, Integrated Villages, and Village Taverns all generated controls. Towns & Towers towns use spacing 51 and separation 12; Better Village uses spacing 45 and separation 20; Village Taverns injects weight-10, limit-1 taverns into five village house pools. Their datapack/registry precedence remains an Item 7 runtime question.
* Loot Integrations uses generated defaults: maps are skipped for added loot, existing items are not skipped, and modded-item weight is 3. Provider-specific integration JARs do not emit separate user configuration.
* ServerCore dynamic adaptation, breeding caps, entity activation range, and special spawning mobcap enforcement are disabled. Its natural monster category remains 70 at a one-tick interval. Its non-parity `reduce-sync-loads` and `cache-ticking-chunks` optimizations are enabled by generated default.
* The materialized server difficulty is `easy`; animal, monster, and NPC spawning are enabled. This is baseline input, not a tuning recommendation.
* C2ME leaves user-facing values at `"default"`. It records that the End biome cache optimization is disabled at runtime due to Biolith 3.0.10 incompatibility. Chunky is retained but generated no config file, which is explicitly different from a generated default.

## Precedence, uncertainty, and downstream gates

There are two global spacing owners, numerous per-provider placements, explicit vanilla replacements, and several village pool/placement owners. The files establish configuration intent but cannot alone prove registry precedence or observed density. Item 7 must inspect fresh worlds for all four deterministic seeds under this exact manifest. Item 10 must quantify Sparse Structures' actual contribution. Loader/mod implicit defaults that produce no file remain identified as implicit or absent rather than fabricated.

Item 7 is eligible only while `uv run python tools/freeze_item6_config.py validate ...` passes. Any configuration mutation creates a new identity and reopens this gate.

## Reproduction

```bash
uv run python tools/freeze_item6_config.py validate \
  --root evidence/item-6/frozen \
  --manifest evidence/item-6/generated-config-manifest.json \
  --audit evidence/item-6/config-audit.json
uv run pytest -q tests/item6
```
