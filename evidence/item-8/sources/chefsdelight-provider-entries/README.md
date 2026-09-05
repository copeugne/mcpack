# Remaining Chef's Delight entry classes

Extractor revision: 060eca4. These four classes complete the archive's six-class
source coverage alongside chefsdelight-villages. Identity manifest SHA-256:
0d3935299b214d7effb7c69d81d798d26979efb3c6b64a75d7bf27c109ccaf09.

```sh
uv run -m tools.inspect_item8_pool_elements --archive chefsdelight-1.0.5-neoforge-1.21.1.jar --class-name 'net/redstonegames/chefsdelight/ChefsDelight$ClientModEvents.class' --class-name net/redstonegames/chefsdelight/Config.class --class-name net/redstonegames/chefsdelight/villager/ModEvents.class --class-name net/redstonegames/chefsdelight/villager/ModVillagers.class --output evidence/raw/item8/chefsdelight-provider-entries-r1
```

Both captures reproduced byte for byte before this README was added. Archive and
class hashes are verified by the existing extractor. Preserve the full trade
method disassembly despite its repetitive size; it is original source evidence,
not a new trade-economy investigation.

ClientModEvents has an empty client setup handler. Config loads the ten village
house weight fields and defines their bounded integer settings. ModVillagers
registers only points of interest and villager professions, using cooking-pot
and skillet block states. ModEvents handles VillagerTradesEvent: it appends
item-cost/item-stack MerchantOffer suppliers to profession trade lists. Its
trade suppliers construct offers; they do not place templates or create a
separate structure-generation path. Existing VillageStructures remains the
village-pool injection implementation.

Next: bind full archive contents and these captures to the provider scope
disposition. No additional house-content, trade-balance or runtime measurement
is required for that candidate-boundary check.
