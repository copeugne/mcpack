# AzureLib Armor entry delegates

Extractor 58a2fd04. Both sources and their manifest reproduce byte for byte
in the independent r1 capture. Manifest SHA-256:
5b79eb326a3e94d744a3f0e9df66028670dab506f8f0a132a40167a868391c07

```sh
uv run -m tools.inspect_item8_pool_elements --archive azurelibarmor-neo-1.21.1-3.1.2.jar --class-name mod/azure/azurelibarmor/common/network/packet/AzItemStackDispatchCommandPacket.class --class-name mod/azure/azurelibarmor/common/render/armor/compat/ShoulderSurfingCompat.class --output evidence/raw/item8/azurelib-armor-delegates-r1
```

The packet finds an existing item animator by identity and dispatches supplied
actions to it. The compatibility initializer only checks whether Shoulder
Surfing is loaded and sets a flag. Neither defines independent generated content.
Consumer animation actions remain the responsibility of the consuming mod.
