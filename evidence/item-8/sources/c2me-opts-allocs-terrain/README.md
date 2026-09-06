# C2ME terrain computation: c2me-opts-allocs-terrain

Extractor f5d6ecb59c7bcf07f7ce09ecfa19861610cb4f20. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
3227a111db5860ff6e682d2c53dd7ad5bb78c26cff2bc5339e244a39efcdc8a3

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-allocs-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/allocs/mixin/MixinIdentifier.class --class-name com/ishland/c2me/opts/allocs/mixin/MixinUtil.class --class-name com/ishland/c2me/opts/allocs/mixin/asm/ASMTargets.class --class-name com/ishland/c2me/opts/allocs/mixin/noise/MixinChainedBlockSource.class --class-name com/ishland/c2me/opts/allocs/mixin/object_pooling_caching/MixinOreFeature.class --class-name com/ishland/c2me/opts/allocs/mixin/surfacebuilder/MixinMaterialRuleContext.class --class-name com/ishland/c2me/opts/allocs/mixin/surfacebuilder/MixinMaterialRulesSequenceBlockStateRule.class --class-name com/ishland/c2me/opts/allocs/mixin/surfacebuilder/MixinMaterialRulesSequenceMaterialRule.class --output evidence/raw/item8/c2me-opts-allocs-terrain-r1
```

Every common hook declared by this module is captured here. This is membership
evidence, not a claim of numerical equivalence or whole-provider closure.

The hooks cache identifier strings, compose existing futures, cache the BitSet
used by existing OreFeature code, and replace collection traversal in existing
noise/surface rule sequences. ASMTargets has no executable contribution beyond
its constructor. These hooks add no authored structure family. The ore hook
changes its temporary BitSet allocation, not the ore definition or placement
registration. Do not expand this into a generic allocation audit.
