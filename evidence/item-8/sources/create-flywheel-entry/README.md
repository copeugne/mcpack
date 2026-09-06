# Embedded Flywheel loader boundary

Extractor: f61db3a86a626e662e114adf03f3a016f170004e.
The full loader disassembly and annotations independently reproduce byte-for-byte.
The Mod annotation explicitly restricts this entry to Dist.CLIENT. This isolated
generated increment supports the embedded rendering-library disposition.

```sh
uv run -m tools.inspect_item8_pool_elements --archive create-1.21.1-6.0.10.jar \
  --nested-archive META-INF/jarjar/flywheel-neoforge-1.21.1-1.0.6.jar \
  --class-name dev/engine_room/flywheel/impl/FlywheelNeoForge.class \
  --output evidence/raw/item8/create-flywheel-entry-r1
```
