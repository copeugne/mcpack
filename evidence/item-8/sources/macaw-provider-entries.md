# Macaw construction provider entry points

Extractor revision 3093a66. Every entry capture and identity manifest reproduced
byte for byte. These verbose captures preserve the complete entry constructor
and annotations, not a keyword-only generation scan.

Paintings has one empty constructor. Doors, Lights and Windows register ITEMS,
BLOCKS, SOUNDS and CREATIVE_TABS on the mod event bus. Fences, Paths, Roofs,
Stairs and Trapdoors register ITEMS, BLOCKS and CREATIVE_TABS. None of these
captured constructors installs a separate generation callback. This is entry
behavior; full archive/resource and other entry-point accounting is still needed
before using it as a complete provider exclusion.

| Entry | Identity manifest SHA-256 |
| --- | --- |
| macaw-doors-entry | db813c5068a8d6fa1b78f112a709df9bc620707bca19d8186bd41a57b8abd2f6 |
| macaw-fences-entry | c99eeaa52cc78326f50612f2b14fce5bfb6230d5fe313399ee76a8187cf7d3b5 |
| macaw-lights-entry | 49a7ebd11aef16ca5dae5c05edf00bdb54ce946446e69d11e0e586f7a81872fe |
| macaw-paintings-entry | c4091c257db20fab47ae561b3dc0125d10f706ad9e2ca3f450d9e855aef7d887 |
| macaw-paths-entry | 4f3d13c6d0fbec8385c7b1d47117763974261d203333253e95ed529b99c4e098 |
| macaw-roofs-entry | 23cfa2081868a72d254ba47cad85cb3ab074ca8bf2c4121e5f9d2fff9956bce5 |
| macaw-stairs-entry | eedc29848482f7d6fc01714dfd9ac845f3b846ef4705ea1d3e0e72b258f5bc26 |
| macaw-trapdoors-entry | 9d198ca0d15d1c937490f37728200a4ec8d03f3f88244c0c0f99f119bca32739 |
| macaw-windows-entry | 932633123c478ee5bee762b1797c881046324410e2e27727659696b5d1a120ec |

Reproduce using the existing extractor:

```sh
uv run -m tools.inspect_item8_pool_elements --archive mcw-doors-1.1.5-mc1.21.1neoforge.jar --class-name com/mcwdoors/kikoz/MacawsDoors.class --output evidence/raw/item8/macaw-doors-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-mcwfences-1.2.1-mc1.21.1neoforge.jar --class-name com/mcwfences/kikoz/MacawsFences.class --output evidence/raw/item8/macaw-fences-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-lights-1.1.5-mc1.21.1neoforge.jar --class-name com/mcwlights/kikoz/MacawsLights.class --output evidence/raw/item8/macaw-lights-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-paintings-1.1.0-mc1.21.1neoforge.jar --class-name com/mcwpaintings/kikoz/MacawsPaintings.class --output evidence/raw/item8/macaw-paintings-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-mcwpaths-1.1.1-mc1.21.1neoforge.jar --class-name com/mcwpaths/kikoz/MacawsPaths.class --output evidence/raw/item8/macaw-paths-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-roofs-2.3.2-mc1.21.1neoforge.jar --class-name com/mcwroofs/kikoz/MacawsRoofs.class --output evidence/raw/item8/macaw-roofs-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-mcwstairs-1.0.2-mc1.21.1neoforge.jar --class-name com/mcwstairs/kikoz/MacawsStairs.class --output evidence/raw/item8/macaw-stairs-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-trapdoors-1.1.5-mc1.21.1neoforge.jar --class-name com/mcwtrpdoors/kikoz/MacawsTrapdoors.class --output evidence/raw/item8/macaw-trapdoors-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive mcw-mcwwindows-2.4.2-mc1.21.1neoforge.jar --class-name com/mcwwindows/kikoz/MacawsWindows.class --output evidence/raw/item8/macaw-windows-entry-r1
```

Scoped extractor Ruff and Basedpyright pass. An initial overlong formatting
line was corrected before the passing checks. No new runtime measurement.
