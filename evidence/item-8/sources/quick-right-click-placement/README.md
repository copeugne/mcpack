# Quick Right Click Placement

Extractor e67cceb7. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
b38d77a4eb459495d5a4addd2db144d784a797d69ac40996e7dc830b6c7484dd

```sh
uv run -m tools.inspect_item8_pool_elements --archive quickrightclick-1.21.1-1.9.jar --class-name com/natamus/quickrightclick_common_neoforge/features/BedBlockFeature.class --class-name com/natamus/quickrightclick_common_neoforge/features/ShulkerBoxFeature.class --class-name com/natamus/quickrightclick_common_neoforge/util/Util.class --output evidence/raw/item8/quick-right-click-placement-r1
```

Held beds and shulker boxes are placed for immediate player use. Bed placement
records prior states, starts sleep and restores on failure or wake; shulker
placement opens its menu and the captured close hook restores state and item.
This is player interaction, not independent world generation.
