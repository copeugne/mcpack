# Supplementaries placement and block processor

Extractor e1e200560c31d0b74a787774db3cf3dc3ddb17d6. Manifest SHA-256:
aaae4d5157a42bdff7bc12d048945a324e3c0c45d8e0bf06edf46a06a7264195.
Independent r1 matches every generated file.

The galleons structure set uses the custom random-spread placement. It rejects
positions within configured exclusion zones by querying existing structure sets.
The block processor transforms disabled blocks within supplied template block
information, preserving its position and NBT. Its replacement record delegates
the toggle to CommonConfigs.isEnabled. These are placement and component
transformations, not independent family generators. This is a contribution-role
finding, not proof of observed placement or effective replacement settings.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RemoveDisabledBlocksProcessor.class --class-name 'net/mehvahdjukaar/supplementaries/common/worldgen/RemoveDisabledBlocksProcessor$Replacement.class' --class-name net/mehvahdjukaar/supplementaries/common/worldgen/RandomSpreadStructurePlacementWithExclusion.class --output evidence/raw/item8/supplementaries-placement-processor-r1
```
