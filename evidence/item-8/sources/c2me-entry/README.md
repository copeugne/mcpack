# C2ME initialization source capture

Extractor ad927f37e207538462db7605d1c75d280e02b759. Independent r1
reproduction matches every disassembly and identity manifest. Manifest SHA-256:
1060789e4b04ae12934bc25e5abf4f398659e99fe5090e80a99ea4c6010f0f69

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/C2MEMod.class --class-name com/ishland/c2me/PreLaunchHandler.class --output evidence/raw/item8/c2me-entry-r1
```

This increment preserves startup and plugin boundaries for provider membership
inspection. It does not assert whole-provider closure or add a family.

C2MEMod invokes the property-controlled prelaunch mixin audit and optional
compression/consistency diagnostics. PreLaunchHandler audits existing mixin
targets through the transformer; these entries do not register content. Do not
run the optional benchmarks as Item 8 evidence. Nested modules remain to inspect.
