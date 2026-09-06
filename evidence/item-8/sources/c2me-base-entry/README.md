# C2ME initialization source capture

Extractor ad927f37e207538462db7605d1c75d280e02b759. Independent r1
reproduction matches every disassembly and identity manifest. Manifest SHA-256:
4ee635a01e2ea82d19f84475bd980a98a753dd0e91ed1808505a7f340f9dc264

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-base-mc1.21.1-0.3.0+alpha.0.93-all.jar --class-name com/ishland/c2me/base/C2MEBaseMod.class --class-name com/ishland/c2me/base/ModuleEntryPoint.class --class-name com/ishland/c2me/base/TheMixinPlugin.class --class-name com/ishland/c2me/base/common/ModuleMixinPlugin.class --output evidence/raw/item8/c2me-base-entry-r1
```

This increment preserves startup and plugin boundaries for provider membership
inspection. It does not assert whole-provider closure or add a family.

C2MEBaseMod registers commonSetup, which flushes configuration. The base
ModuleEntryPoint evaluates executor parallelism configuration. TheMixinPlugin
delegates selection to ModuleMixinPlugin. That shared plugin initializes
MixinExtras and reflectively loads the package-associated ModuleEntryPoint,
reads its enabled field, and uses that value for shouldApplyMixin. getMixins
returns null and preApply/postApply are empty. Therefore the next membership
boundaries are the module entrypoints and content-relevant hooks, not a
general configuration-parser or executor audit.
