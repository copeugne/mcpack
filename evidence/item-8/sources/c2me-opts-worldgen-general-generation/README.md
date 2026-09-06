# C2ME generation hooks: c2me-opts-worldgen-general-generation

Extractor 736d66fa99506e243106ed8b93d63410546b5417. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
e0bc55aa54c629fbc6eba04c75964ad08a556085ca4edfcb5f04db524f7becdc

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-worldgen-general-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/worldgen/general/mixin/random_instances/MixinAtomicSimpleRandomFactory.class --class-name com/ishland/c2me/opts/worldgen/general/mixin/random_instances/MixinRedirectAtomicSimpleRandom.class --class-name com/ishland/c2me/opts/worldgen/general/mixin/random_instances/MixinRedirectAtomicSimpleRandomStatic.class --output evidence/raw/item8/c2me-opts-worldgen-general-generation-r1
```

This capture retains the pool/generation boundary for membership inspection.
It does not establish whole-provider closure or unchanged generation outcomes.

These hooks replace random-source factories and constructors used by existing generation. They do not register a new feature or family. This is not proof that random sequences or generated outcomes are unchanged.
