# C2ME startup delegates: c2me-rewrites-chunk-system-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
8f8b84d8966e7d8844710905d470d2d6b3b73ee4015860e76800c04aab20ab94

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-rewrites-chunk-system-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/rewrites/chunksystem/common/Config.class --output evidence/raw/item8/c2me-rewrites-chunk-system-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration reads chunk-system, fluid-postprocessing and serialization settings. It does not register content.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
