# Adorabuild End ship: quality assessment

Status: selected fixed case locally assessed under the authorized modeled and
inspection scope. One complete occurrence satisfies this fixed-root sampling
minimum. Whole Item 13 coverage and reviewed delivery remain IN PROGRESS.

## Evidence identity and surface check

Sample: full-ordinary-r1-baseline|minecraft:the_end|adorabuild_structures:end_ship_small_1|505|508.
[Raw blocks](adorabuild-end_ship_small_1.json.gz), SHA-256
ce8ce3d9a97fb35de7a7cd321801842a592c678910344dfa5fec667ee062badd,
retain envelope [8080,56,8116,8084,65,8128] and padded bounds
[8077,53,8113,8087,68,8131]. Source identity, transform and locked extraction
receipts are in the [batch intake](README.md#remaining-four-selected-adorabuild-inputs).
No world was changed and no new server experiment was run.

The [ten-layer sheet](adorabuild-end_ship_small_1-slices.png) shows an open deck,
central mast and elevated decorative spar. The first sheet's narrow panels made
coordinate labels overlap. That [rejected image](adorabuild-end_ship_small_1-slices-rejected-labels.png)
is preserved: conversion 0.69 seconds, 385,419 SVG bytes and 48,603 PNG bytes.
The existing renderer now gives panels a minimum width of 330 pixels, resolving
this demonstrated labeling defect without changing block data. Corrected
conversion took 0.74 seconds (0.75 user, 0.02 system), with 385,844 SVG bytes and
52,849 PNG bytes, 438,693 combined. Both attempts together took 1.43 conversion seconds and
872,715 SVG/PNG bytes, within the declared 30-second/2-MiB case cap. The corrected image was inspected and labels are clear.
Focused renderer Ruff and basedpyright checks pass. Existing historical figures
are not regenerated merely because their producer now has this display fix.

## Playable topology and complete route

R1 is one open activity deck, principally X8081..8083,Z8119..8125, feet Y58,
with a central full mast at (8082,58+,8122) and half-block bow/edge details.
Count one outdoor activity area, zero enclosed rooms. The source's ten vertical
layers are not ten floors. The spar above Y62 has no authored connected ascent
or distinct objective and is not counted as another room.

Use one adult width0.6/height1.8, ordinary step capability, full layout knowledge.
Start at the western deck edge (8080.5,58,8122.5). The top-half east-facing stair
below at (8080,57,8122) has full support at Y58; body cells above are air. Travel
to this staged local edge is excluded, not assigned zero exploration cost.
Move one east to (8081.5,58,8122.5), then three north to the combat station
(8081.5,58,8119.5). The X8081 lane has full obsidian support at Y57 and air at
Y58..61 throughout Z8119..8125. The centered body clears the mast's X8082 face
by 0.2 blocks. The eastern X8083 lane also has full support and air Y58..59,
so the mast is an obstacle with two local ways around it, not a room partition.

After the conditional encounter, move one north onto the bottom slab at
(8081,58,8118), feet Y58.5. Its supporting top stair at Y57 and air above give
a supported half-block step. The whole body footprint stays within X8081,
clear of the central bow stair and the shulker's authored cell. From eye
(8081.5,60.12,8118.5), target the dragon head's west face at
(8082.25,59.5,8116.75). Pinned WallSkullBlock's north-facing shape is local
[.25,.25,.5,.75,.75,1]. The 2.002349-block ray reaches that face; it stays
X<8082 until Z<8117, avoiding the raised central bow stair. Its earlier cells
in X8081 at Y59/60 are air. It is ordinary interaction reach, not demonstrated
pickup. Mine the head with the declared pickaxe, then acquire it under the
approved conditional four-block pickup excursion and acquisition allowance.

Return one south/down to the combat station and continue six south to chest
station (8081.5,58,8125.5). The chest's west inset face is
(8082.0625,58.5,8125.5), 1.253318 blocks from eye Y59.62, through air before
the chest. The saved single north-facing chest has air at (8082,59,8125), no
Lock and no generated Items. Under the no-blocking-entity scenario it opens.
Transfer its contents using the accepted 29 menu operations and inventory check.
Return three north to the mast-side hub, then one west to the start.

The connected circuit has **16 horizontal blocks, 0.5 ascent and 0.5 descent**,
plus four conditional pickup blocks, hence 20 modeled horizontal blocks. The
half-block step uses the existing 1/.5/.25 vertical-step-speed sensitivity,
separately from horizontal travel. No doors, bridge, flight, tunneling or mast
climb is needed. No ordinary decorative purpur/obsidian salvage is part of the
reward objective. The dragon head is included because it is a distinct trophy.

## Enemy potential and source mechanics

The single template resident is a shulker, Health30, Peek30, transformed authored
position (8082.5,58,8118.5). No spawner block exists. This is **one authored enemy
and one authored type**, not one observed living enemy. The source placement
cell contains a bottom north-facing stair at Y58; its lower half overlaps the
nominal closed shulker body. Do not silently treat that source coordinate as a
validated stable encounter. Saved entity state, survival, attachment changes and
settled population remain NOT MEASURED. Legacy template attribute spellings do
not establish loaded attributes.

Pinned source: Minecraft SRG jar SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Shulker.createAttributes sets health30. setRawPeekAmount removes the covered
armor modifier, adding it for zero peek; the static modifier adds armor20.
CombatRules.getDamageAfterAbsorb uses effective armor
clamp(armor - damage/(2+toughness/4), armor*.2, 20), then damage*(1-effective/25).
For ordinary armor0/toughness0, an unenchanted six-damage sword needs five hits.
For armor20/toughness0 it deals 1.92 damage and needs sixteen hits. At thirteen
ticks per reserved full attack, these are 3.25 and 10.4 active seconds. They
are attack-state endpoints, not probabilities of being open or closed.

Shulker.hurt can attempt teleport below half health when nextInt(4)==0. The
teleport routine tries positions offset up to eight blocks on each axis, with
attachment/space checks. findNewAttachment also has a teleport fallback.
ShulkerBullet.onHitEntity attempts four damage and, after successful damage to a
living entity, adds levitation for 200 ticks. These support meaningful projectile,
displacement and changed-position hazards. The model below does not predict
injury, successful teleport frequency, safe levitation recovery or survival.

## Conditional complete-task timing

Apply the approved A/B/C cost accounting, full-health/food adult, unenchanted
iron armor/sword and diamond pickaxe, sufficient durability and free inventory,
20 TPS and known targets. No buffs, criticals, sweeps, healing or external help.
For the one-enemy scenario, stipulate one ordinary shulker settled on the clear
full-supported deck cell (8082.5,58,8119.5), bottom attachment, health30. This is
an explicitly chosen viable encounter input, **not an observed relocation from
the clipped authored position**. Clear it from the adjacent named combat station
before the head/chest phases. Duty includes targeting, waiting for attack state,
defense/repositioning and return to that station. No successful teleport,
levitation or additional entity is permitted in this successful scenario.

Use open-hit and closed-hit armor endpoints separately. Mixed armor histories
within these assumptions lie between their attack-work totals; this is not a
bound on unrestricted live combat. One unresolved or absent resident instead
has no measured clear time; do not substitute the one-enemy scenario for a census.

Pinned Blocks registers dragon_wall_head with strength1 and dropsLike dragon_head.
It is absent from the pinned pickaxe mining tag, so the ordinary declared pickaxe
has speed1: ceil(1*30/1)=30 ticks, **1.5 mining seconds**. No correct-tool-only
requirement is declared for this head. Its base loot table names one dragon_head;
generated or acquired items remain NOT MEASURED.

| Task component | Complete accounting |
| --- | --- |
| Travel | 16 checked horizontal plus 4 conditional pickup blocks; .5 up and .5 down |
| Decisions | 8: entry orientation, combat station, encounter completion, bow step/head, pickup/return, chest, hub return, exit |
| Interactions | 30: one mining initiation and 29 single-chest menu operations |
| Selections | Two: sword before combat, pickaxe before head |
| Acquisition | Two allowances: head pickup and chest inventory confirmation |
| Mining | 1.5 seconds for head; no construction |
| Combat | 3.25 or 10.4 active seconds divided by A/B/C contact duty |
| Completion | One verification allowance: both rewards acquired, stipulated enemy cleared, live return |

Noncombat budgets are **22.5/40.5/72.166667 seconds**. With one shulker and all
hits during armor0 states, complete totals are **25.75/44.833333/78.666667**;
with all hits against armor20, **32.9/54.366667/92.966667**. Report approximately
**26..33 / 45..54 / 79..93 seconds**, keeping profiles and attack states visible.
These are successful conditional budgets, not first-clear averages or calibrated
player outcomes. Pickup beyond the assumed excursion, failed inventory transfer,
death, required healing, teleport, levitation, extra entities, invalid combat
station/return, out-of-budget attack duty or changed tick/input conditions censor
the model. No trial with these conditions has been observed.

## Remaining quality dimensions

The activity graph has one node, no inter-room edges, no degree-three room
junctions and no room-graph cycles. Local paths around the mast are a geometric
loop within that area, explicitly retained instead of counted as new rooms.
The two one-cell side lanes are about one block wide with at least two blocks
of clear headroom; the declared centered actor fits. Neither is the only way to
the bow. Deepest room depth is zero graph edges; head interaction station is
five horizontal blocks from entry plus the half step, chest station four.

Empty/dead activity areas: **0/1**, supported by the two distinct reward nodes
and authored enemy potential. Strict enclosed-room empty/dead fractions are N/A
with denominator zero, not zero-percent evidence. No additional inaccessible
mast cavity is counted as a dead room. The selected geometry has no void below
the checked deck: end stone occurs at Y56 across these support columns. Bare
perimeter columns likewise show ground at Y56. The tall mast and nearby terrain
are not terrain burial; no far-away island approach or fall outcome is measured.

Loot distribution is one chest toward the stern and one dragon-head trophy at
the bow, both in the same open activity area. The base End-city treasure table,
SHA-256 085031a52e0ada20df65d9dd9bf9a61a2da6ae33a403c1c34fd26539947a2ef2,
has resource/enchantable equipment alternatives and a spire-trim alternative.
The head block table SHA-256 is
93d038b0b66cca0fe72609e588195ad385a3fd71ef21b86948281c5f7d67ab2f.
Both are precise entries in the pinned extra jar, SHA-256
24a5d2d162cfad2a1a574c4d552e99dc6c6303a49d1e68b43a7b638f3b0930fd.
Table opportunities are not actual rolled value or current-player acquisition.
No elytra item frame or other elytra reward is authored in this one-entity template.

Finale NONE: there is no separate terminal room, boss or completion trigger.
Reward clarity is PRESENT (display chest and trophy); distinctive terminal
challenge and ordered room progression are ABSENT; live enemy/reward linkage is
CONDITIONAL on realization and AI. External exposure is PRESENT. From the same
edge, one east and three south reaches the chest, then return: eight horizontal
blocks, no excavation, skipping the bow phase. This proves a partial-objective
route bypass, not that a live shulker cannot interfere or that every outside
approach is safe. Full modeled completion still includes both reward nodes.

Expected replay variation is limited in authored topology: fixed open deck and
one resident type, with chest rolls and realization/surroundings as varying inputs.
No self-reset is authored in the inspected template. Persistence, loot refresh
and player willingness to revisit are not invented. Relative to the ten-layer
mast silhouette, playable progression is mechanically shallow, but the shulker's
supported special mechanics prevent equating shallow topology with harmlessness.
This case satisfies the local fixed-family assessment minimum; Item 13's other
families, material variants and full review/merge gate remain open.

## Reproduction

Reuse the batch source extraction and pinned javap procedure for Shulker,
ShulkerBullet, CombatRules, WallSkullBlock and Blocks. The exact methods and
resource paths above reproduce direct inspections without a new server trial.

```sh
uv run python -m evidence.item-13.render_pilot --input evidence/item-13/fixed-blocks/adorabuild-end_ship_small_1.json.gz --output /tmp/item13-end-ship.svg
timeout 30 convert -background white /tmp/item13-end-ship.svg /tmp/item13-end-ship.png
uv run python - <<'END_SHIP'
import gzip, hashlib, importlib, json, math
from pathlib import Path
raw = Path('evidence/item-13/fixed-blocks/adorabuild-end_ship_small_1.json.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'ce8ce3d9a97fb35de7a7cd321801842a592c678910344dfa5fec667ee062badd'
c = json.loads(gzip.decompress(raw))['cases'][0]
s = importlib.import_module('evidence.item-13.render_pilot').state_at
for z in range(8119,8126):
    assert s(c,8081,57,z)['Name'] == 'minecraft:obsidian'
    for y in (58,59,60):
        assert s(c,8081,y,z)['Name'] == 'minecraft:air'
assert s(c,8081,58,8118)['Properties']['type'] == 'bottom'
assert s(c,8082,59,8125)['Name'] == 'minecraft:air'
print('head ray',math.dist((8081.5,60.12,8118.5),(8082.25,59.5,8116.75)))
print('chest ray',math.dist((8081.5,59.62,8125.5),(8082.0625,58.5,8125.5)))
closed_damage = 6*(1-(20-6/2)/25)
assert math.ceil(30/closed_damage) == 16
for name,u,step,n,a,sel,k,v,d in [
        ('A',5,1,.5,.25,.25,1,2,1),('B',4,.5,1,.5,.5,2,4,.75),
        ('C',3,.25,1.5,1,1,4,8,.5)]:
    base = 20/u+1/step+1.5+8*n+30*a+2*sel+2*k+v
    print(name,'noncombat',base,'open-hit full',base+3.25/d,'closed-hit full',base+10.4/d)
END_SHIP
```
