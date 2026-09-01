# Item 9 — Provisional Baseline Structure Classification

**Status:** `COMPLETE`
**Scope:** zero-mod vanilla control
**Decision state:** provisional diagnosis only; no retention/removal decision

## Classification result

Every one of the 21 Item 8 gameplay families has exactly one primary role:

| Category | Count | Families |
|---|---:|---|
| Tier 0 — Ambient Landmark | 4 | igloo, shipwreck, Nether fossil, ruined portal |
| Civilization | 1 | village |
| Tier 1 — Small Encounter | 8 | pillager outpost, mineshaft, jungle temple, desert pyramid, swamp hut, ocean ruin, buried treasure, trail ruins |
| Tier 2 — Proper Dungeon | 1 | trial chambers |
| Tier 3 — Major Expedition | 5 | woodland mansion, ocean monument, End city, bastion remnant, ancient city |
| Tier 4 — World Objective | 2 | stronghold, Nether fortress |

The classification validator proves 21 expected and 21 classified families, no duplicates, no omissions, no invalid category and a non-empty rationale for every family.

## Interpretation rules

- The tier describes the family's primary gameplay role, not its physical size or maximum time spent.
- Large does not mean “proper dungeon.” Mineshafts are large networks of repeated small encounters and therefore remain Tier 1 with a mechanical-shallowness flag.
- Required progression destinations may be Tier 4 even when their encounter topology is weak. Strongholds and Nether fortresses are world objectives because they gate End/Nether capability progression.
- Non-combat search/excavation can exceed Tier 0 when it has a meaningful objective/reward. Buried treasure and trail ruins are Tier 1.
- A biome palette is not a separate gameplay family. Five villages, seven ruined portals, two shipwrecks, two ocean ruins and two mineshafts remain internal variants.

## Flagged deficiencies

### Dungeon-like but mechanically shallow

- Mineshaft: oversized procedural network, repetition, no finale.
- Swamp hut: hostile dressing with almost no traversal/gameplay volume.
- Stronghold: progression objective with repeated corridors and limited authored combat.
- Nether fortress: progression objective with repeated corridors and no authored multi-phase finale.

### Oversized relative to internal gameplay

- Mineshaft is the clearest baseline case.
- Woodland mansion has real expedition scale but substantial room repetition and a weak/variable finale.

### Mostly decoration or ambient by design

- Nether fossil is primarily decorative.
- Igloo, shipwreck and ruined portal intentionally serve ambient/salvage roles rather than pretending to be dungeons.

### Concentrated value or weak distribution

- Desert pyramid and buried treasure concentrate value in one small target.
- End city and bastion reward value can concentrate heavily by generated archetype/ship/treasure room.
- Ocean monument has strong salvage/objective value but weak conventional chest-loot distribution.

### Discoverability concern

- Ancient cities and trial chambers lack assured surface discovery language.
- Trail ruins expose only a small cue.
- Strongholds and buried treasure are intentionally lead/map dependent.

## Redundancy result

No baseline gameplay family is provisionally redundant because the zero-mod control contains no overlapping third-party structure generators. Internal biome/environment variants are consolidated under one family. Procedural-corridor repetition overlaps among mineshafts, strongholds and fortresses, but their primary roles differ. Trial chambers remain distinct through encounter infrastructure.

This does **not** protect vanilla content from later replacement or pruning. It only means redundancy cannot be claimed within the current control without measured evidence.

## Machine record

- `structure-inventory/item9-provisional-classification.json` records every rationale and defect flag.
- `evidence/structure-inventory/item9-classification-verification.json` proves total/exact family coverage.

## Exit decision

All baseline families have one provisional primary role and every requested deficiency/redundancy class has a recorded disposition. No final solution or mod selection was made. Item 10 may now measure actual baseline structure/encounter density using these family/category identities.

