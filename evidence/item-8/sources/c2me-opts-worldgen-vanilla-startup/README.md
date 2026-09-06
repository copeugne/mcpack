# C2ME startup delegates: c2me-opts-worldgen-vanilla-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
393467d9540ea5362f62e682fa86bebdd89c60072a9f8ca68ed706d34130e1bd

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-worldgen-vanilla-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/worldgen/vanilla/common/Config.class --output evidence/raw/item8/c2me-opts-worldgen-vanilla-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration reads aquifer, End biome cache and structure-weight optimization settings. These control already captured hooks, not another structure family.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
