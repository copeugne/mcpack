# Creating Space common-hook delegates

Extractor 30d63026469e22adedd6b9809149a6b4dd96ea01. Manifest SHA-256: 452f56f08a577286fe894d2e692aa26b73e67dda6027274c318fcb30c7c7145e. Independent r1 matches every generated file.

These four delegates resolve the fluid-interaction registration, dimension-data updates, oxygen-room regeneration and saved-design loading called by the captured common entries. They use the existing source extractor, without a new runtime measurement.

```sh
uv run -m tools.inspect_item8_pool_elements --archive creatingspace-1.21.1-1.7.18.jar --class-name com/rae/creatingspace/init/ingameobject/FluidInit.class --class-name com/rae/creatingspace/content/planets/CSDimensionUtil.class --class-name com/rae/creatingspace/content/life_support/sealer/RoomAtmosphere.class --class-name com/rae/creatingspace/legacy/saved/UnlockedDesignManager.class --output evidence/raw/item8/creating-space-common-delegates-r1
```
