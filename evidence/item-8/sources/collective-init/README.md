# Collective initialization delegates

Extractor 1d0366c7. Seven classes. Independent r1 reproduction matches all
source and manifest bytes. Manifest SHA-256:
aebbe9220eb37a9142a499b1b3a817fa83e76c846586983a3627c91a1eb6138f

```sh
uv run -m tools.inspect_item8_pool_elements --archive collective-1.21.1-8.25.jar --class-name com/natamus/collective/neoforge/networking/NeoForgeNetworkHandler.class --class-name com/natamus/collective_common_neoforge/check/RegisterMod.class --class-name com/natamus/collective_common_neoforge/config/GenerateJSONFiles.class --class-name com/natamus/collective_common_neoforge/config/LoadJSONFiles.class --class-name com/natamus/collective_common_neoforge/data/Constants.class --class-name com/natamus/collective_common_neoforge/data/GlobalVariables.class --class-name com/natamus/collective_common_neoforge/implementations/networking/NetworkSetup.class --output evidence/raw/item8/collective-init-r1
```

GenerateJSONFiles materializes requested configuration data and notifies
consumer callbacks. LoadJSONFiles reads name/message lists. GlobalVariables
starts consumer entity-replacement lists empty and initializes shared lookup
data. Constants prepares item/enchantment lookup stacks. Network setup handles
consumer-supplied packets/actions. RegisterMod records mod metadata and checks
for updates. None defines an independent generated site. Preserve operational
update checking; this is not a network or consumer-handler safety audit.
