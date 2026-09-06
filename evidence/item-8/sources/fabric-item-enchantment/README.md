# fabric-item-enchantment source roles

Extractor e957cf9. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: d653028574d440be486250233dd9364855a141a5da678dbc6f3ff23338104e31.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-item-api-v1-11.2.0+0c57911319.jar --class-name net/fabricmc/fabric/impl/item/EnchantmentUtil.class --output evidence/raw/item8/fabric-item-enchantment-r1
```

The loading delegate copies an existing enchantment definition, exclusive set and effects, forwards EnchantmentEvents.MODIFY, and rebuilds that supplied enchantment. Source classification distinguishes vanilla, mod and data-pack inputs. No independent structure family is introduced.
