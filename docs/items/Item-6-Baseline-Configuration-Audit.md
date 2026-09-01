# Item 6 — Pristine Baseline Configuration Audit

**Status:** `COMPLETE`
**Audit mode:** read-only
**Baseline:** zero third-party mods

## Scope correction

The supplied 190-JAR list is tentative, and the user confirmed no installed instance existed. Item 6 therefore audits the only honest baseline: Minecraft 1.21.1, NeoForge 21.1.249, no third-party JARs. It does not infer configuration for draft candidates, and it changes no settings.

The independently booted Item 4 restore instance is the generated-default reference. All three platform TOML files match it byte-for-byte. `server.properties` differs only in its generated timestamp comment and matches after timestamp normalization.

## Existing configuration inventory

| Surface | State | Disposition |
|---|---|---|
| `config/fml.toml` | NeoForge-generated; exact independent-reference match | Default, no change |
| `config/neoforge-common.toml` | NeoForge-generated; exact independent-reference match | Default, no change |
| `config/neoforge-server.toml` | NeoForge-generated; exact independent-reference match | Default, no change |
| `server.properties` | Minecraft-generated; independent normalized match | Default, no change |
| `user_jvm_args.txt` | Explicit construction envelope: `-Xms1G`, `-Xmx4G` | Non-default project value; testing only |
| `eula.txt` | `eula=true` after explicit user acceptance | Required authorized change |
| `defaultconfigs/` | Empty | No overrides |
| `world/datapacks/` | Empty | No datapacks |
| `mods/` | Empty | Zero-mod baseline confirmed |
| access-control JSON | Empty ops, whitelist and ban lists | Baseline state, not final operations policy |

## Requested candidate surfaces

| Requested audit family | Baseline result |
|---|---|
| Sparse Structures | Not installed; no config exists |
| Structure Essentials | Not installed; no config exists |
| ServerCore | Not installed; no config exists |
| C2ME | Not installed; no config exists |
| Chunky | Not installed in pristine baseline; no config exists |
| Structure Layout Optimizer | Not installed; no config exists |
| When Dungeons Arise / Seven Seas | Not installed; no config exists |
| YUNG family | Not installed; no config exists |
| IDAS / Integrated family | Not installed; no config exists |
| Moog families | Not installed; no config exists |
| village generators | Not installed; no config exists |
| Loot Integrations | Not installed; no config exists |
| modded mob spawning/difficulty | Not installed; only vanilla server properties exist |

“No config” is not a compatibility or suitability conclusion. Every retained candidate will receive its own generated-config audit when admitted to an experimental branch.

## Platform values relevant to later design

These are unmodified defaults, but they can materially affect the intended pack and are flagged without changing them:

| Key | Baseline | Later owner |
|---|---:|---|
| `difficulty` | `easy` | Items 14, 25–27, 44–45 |
| `pvp` | `true` | Cooperative/consensual-PvP operations design |
| `allow-flight` | `false` | Aeronautics runtime test; do not assume mod flight bypasses vanilla checks |
| `view-distance` / `simulation-distance` | `10` / `10` | Performance and discoverability protocols |
| `max-players` | `20` | Final value should reflect declared 10-player peak plus policy |
| `generate-structures` | `true` | Required baseline worldgen behavior |
| `sync-chunk-writes` | `true` | Item 17/49 storage and save testing |
| `max-tick-time` | `60000` ms | Operations/watchdog design |
| `spawn-monsters` / `spawn-npcs` | `true` / `true` | Baseline combat/civilization behavior |
| `spawn-protection` | `16` | Claims/griefing and spawn policy |
| `white-list` / `enforce-whitelist` | `false` / `false` | Final access-control policy |
| `log-ips` | `true` | Privacy/log-redaction policy |

NeoForge safety defaults `removeErroringEntities=false` and `removeErroringBlockEntities=false` preserve crash evidence instead of silently deleting state. `dependencyOverrides={}` proves no compatibility constraint is bypassed.

## Non-default values

Only two deliberate deviations exist:

1. EULA acceptance, explicitly authorized by the user.
2. The construction-only 1–4 GiB heap envelope.

No hidden global structure multiplier, per-structure override, disabled structure set, modded spawn rule, loot override, or difficulty mod exists in the baseline. Therefore none can explain later candidate-stack density until actually installed.

## Exit decision

The complete existing configuration surface is inventoried and hash-retained in `evidence/config-audit/item6-pristine-config-audit.json`. Every named absent surface is explicit. No setting was changed. Item 7 may evaluate the zero-mod terrain/worldgen control; modded interactions belong to controlled candidates after admission.

