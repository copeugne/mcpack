# C2ME startup delegates: c2me-opts-chunkio-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
f2cf4564f5c470322835e8dec3c20815d0ad3c57ab678100651933612f25eaec

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-chunkio-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/chunkio/common/Config.class --output evidence/raw/item8/c2me-opts-chunkio-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration initializes the existing chunk-I/O cache setting through the base config accessor. It does not register content.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
