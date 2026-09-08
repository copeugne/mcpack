# BetterEnd r2: incoming runtime class inspection

The predeclared 324-chunk pilot completed under source
`0b1adc3ce75b5ea74eba26bec8b38c033eeb6166` in 89.21 seconds. The
[diagnostic receipt](diagnostic.json) records frozen preflight, all four selections,
configuration validation, correlated save-flush and clean exit 0. The
[trace](trace.jsonl) records all five installations and a clean shutdown with
zero unfinished attempts. There were no feature attempts in this small region;
this run supplies class inspection evidence, not placement or density validation.

All five incoming class files were retained before the probe transformed them.
Each file's SHA-256 matches its installation record. The three BetterEnd classes
and scarecrow match their packaged Item 8 identities. Incoming Minecraft
`StructureTemplate` has SHA-256
`a200a7b594c4ca604f3c8074051d34822a6d96abf223c9f58c261e0e146d5a28`.
This is different from both the packaged class and r1's incoming hash. Since r1
never retained incoming bytes, the precise r1-to-r2 difference remains UNKNOWN.
Do not backfill r1 or assume one constant incoming hash for later runs.

## Direct inspection of the retained class

The raw archive retains `StructureTemplate-incoming.txt`, produced with:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c evidence/raw/item10/betterend-identity-r2/trace.jsonl.classes/net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplate.class
```

Compare with the packaged disassembly in
`evidence/item-8/sources/missing-template-code`. The incoming class includes
accessor interfaces for Repurposed Structures, Integrated API and Moog's Structures;
C2ME initializes synchronized lists; Railways adds serialization handling.
Within `placeInWorld`, the relevant observed differences are:

- Better Dungeons initializes its context at method entry (offset 11).
- Structure Layout Optimizer selects the in-bounds block list through its bridge
  at offset 78. The bridge reads the position/settings references and delegates
  to `getStructureBlockInfosInBounds`.
- The processor call at offset 270 uses the overload receiving this template.
- Zeta applies its block-state replacement at offset 375, before content writing.
- The three direct `ServerLevelAccessor.setBlock` calls remain barrier at 412,
  content at 425, and subsequent update at 1139. The content call consumes world,
  position, resulting state and original flags, then branches on refusal at 430.

The existing probe's second-call-site hook therefore observes the content write
in this captured runtime class, including the resulting Zeta state. It leaves
those surrounding operations in place. This finding is specific to the retained
bytes and does not validate uninspected future transformations or prove runtime
placement capture. Future differing inputs require inspection before acceptance.
No gameplay configuration was changed; r1 remains rejected and the full collector
gate still requires positive runtime observations and saved-world corroboration.

## Verified raw custody

The [immutable release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-identity-2026-09-08-r2)
is bound to the launch revision by its fetched tag. Its 5,113,881-byte archive
has SHA-256 `ecaad334886bf659a9685721be64f03c911b36cfd6b766b787ec8f58340c35a5`.
The [download/restore receipt](download-restore.json) verifies 255 raw files,
including all captured classes and the disassembly. The downloaded manifest is
byte-identical. The [nested world restore](world-restore.json) has all 96 expected
paths with matching sizes and hashes; it was not booted.

The generated manifests are retained with this one diagnostic result. Creation
and verification use the existing tools:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/betterend-identity-r2 --archive evidence/raw/item10/betterend-r2-custody/item10-betterend-identity-r2-0b1adc3c.tar.gz --manifest evidence/item-10/betterend-identity-r2/archive-manifest.json --revision 0b1adc3ce75b5ea74eba26bec8b38c033eeb6166
gh release download item-10-betterend-identity-2026-09-08-r2 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-betterend-identity-r2-0b1adc3c.tar.gz --manifest evidence/item-10/betterend-identity-r2/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 916d36e97ec13af45b76b5a06fe9edf6b1d0c8aa8f40ded4129dab853faf858d --target RESTORED_WORLD
```
