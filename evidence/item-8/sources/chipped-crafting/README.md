# Chipped crafting handler

Extractor 03922316. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
d534c942c6ea84ba30074d4772816b49b2e94498cf9824ed64225e0415446b53

```sh
uv run -m tools.inspect_item8_pool_elements --archive chipped-neoforge-1.21.1-4.0.2.jar --class-name 'earth/terrarium/chipped/common/network/ServerboundCraftPacket$Type.class' --output evidence/raw/item8/chipped-crafting-r1
```

The handler requires the player's current menu to be a WorkbenchMenu, invokes
its crafting action and broadcasts container changes. This is player crafting,
not a generated-site entry point. No further networking audit is needed for
family membership.
