# Accessories initialization and event delegates

Extractor 3a39673a9e6cc52b7c06e7d384aaaf28f8585923. Independent r1 reproduction
matches both disassemblies and the identity manifest. Manifest SHA-256:
599e8339dcb834199a136be2b53e9063cf2a62cb5560db04e9680e9e3dacbaef

```sh
uv run -m tools.inspect_item8_pool_elements --archive accessories-neoforge-1.1.0-beta.53+1.21.1.jar --class-name io/wispforest/accessories/Accessories.class --class-name io/wispforest/accessories/impl/AccessoriesEventHandler.class --output evidence/raw/item8/accessories-startup-r1
```

Accessories.init installs custom-renderer support, entity-modification callback
and armor-slot types. AccessoriesEventHandler operates on existing accessory
containers and living entities. onWorldTick reaches player revalidation after
reload; entityLoad synchronizes existing player containers. Equipment ticking,
drops and tracking preserve accessory state/effects, not independent worldgen
structures. No generic packet, renderer or equipment implementation audit is
needed once this contribution role is established.

Use with accessories-provider and complete packaged payload binding for the
whole-provider membership decision. Preserve the existing inventory, loot,
entity and NBT effects rather than claiming no gameplay impact.
