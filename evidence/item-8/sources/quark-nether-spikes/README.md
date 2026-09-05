# Quark Nether obsidian spikes

Captured with extractor revision b9f1cc8. identities.json binds both verbose
captures to the retained Quark archive. Both captures and identities reproduced
byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/NetherObsidianSpikesModule.class --class-name org/violetmoon/quark/content/world/gen/ObsidianSpikeGenerator.class --output evidence/raw/item8/quark-nether-spikes-b9f1cc8
```

## Registration and initial settings

The module's LoadEvent setup registers ObsidianSpikeGenerator with Zeta at
UNDERGROUND_DECORATION, weight 10. Its world category annotation has no overlap
entries. All five settings have Config annotations. The existing shared Quark
category, annotation conversion, field mapping and initial-refresh evidence
therefore applies without a new library investigation. The retained debug log
records construction as Nether Obsidian Spikes at line 13906. The frozen module
toggle is true at line 768. The matching world.nether_obsidian_spikes section
at lines 1164 through 1175 sets chancePerChunk=0.1, bigSpikeChance=0.03,
triesPerChunk=4, bigSpikeSpawners=true and a Nether dimension allowlist.
Source defaults agree. These are initial source/config/log-derived settings,
not observed frequencies. Frozen Quark file identity and equality to the loaded
file are already preserved in quark-monster-box-bindings.

## Placement and geometry

generateChunk draws one float against chancePerChunk. On success it makes
triesPerChunk attempts at random local X/Z in 0 through 15, offset Y=50 from
the supplied chunk corner. Each scans downward while Y>10 until the first
Blocks.LAVA target, invokes placeSpikeAt and ends that attempt. No biome filter
appears in this direct generator. Lava detection is not proof placement succeeds.

placeSpikeAt chooses section heights a=3+nextInt(3), b=2+nextInt(4), and
c=2+nextInt(3). A successful bigSpikeChance draw adds 7, 8 and 4 respectively,
and enables the encounter branch only if bigSpikeSpawners is true. It first
requires every position in a 5 by 5 box, from target Y through Y+a+b+c+1,
to be air or source/flowing lava. Other contents abort placement.

The base writes a 3 by 3 obsidian column from relative Y=-10 through a-1,
skipping positions whose destroy speed is -1. The middle writes its center and
positions in MiscUtil.HORIZONTALS for b layers. The tip writes its center for
c layers. Thus requested vertical extent is a+b+c+10: 17 through 24 blocks
for ordinary spikes and 36 through 43 for large spikes. Ten layers extend
below the lava target. These are source envelopes, not measured occupied sizes;
the base can skip blocks and setBlock return values are discarded. The middle
direction array contents are not independently bound by this capture.

## Encounter and reward content

On the first tip layer of the large encounter branch, the center becomes
CompressedBlocksModule.blaze_lantern when that module and enableBlazeLantern
are enabled, or glowstone otherwise. One block below, the generator places a
physical minecraft:spawner and sets its entity type to BLAZE. One further block
below, it places a chest and, if its block entity is a randomizable container,
assigns BuiltInLootTables.NETHER_BRIDGE. The source does not directly spawn
entities. The spawner cast is unguarded, and placement return values are ignored;
no observed successful encounter is asserted. Smaller spikes do not enter this
spawner/chest branch. There are no structure templates or authored rooms.

The distinct encounter branch must remain explicit in the eventual family
record, even if sizes are retained as variants of one spike design. Resolve
the selected loot-table identity and decoration dependency from existing
evidence where possible, then integrate the working family. No final family
count, natural-spawn composition or saved-world occurrence is established here.

Scoped extractor Ruff and Basedpyright checks passed. No new measurement
system or server run was added.
