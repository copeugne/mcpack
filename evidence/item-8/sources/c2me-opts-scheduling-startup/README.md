# C2ME startup delegates: c2me-opts-scheduling-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
f8d52df46dd47285ed8c0bf6cf2066a3937ee25914bb4e716c611fa5fd44fc43

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-scheduling-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/scheduling/common/Config.class --output evidence/raw/item8/c2me-opts-scheduling-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration initializes task timing and autosave mode through the base config accessor, with explicit compatibility conditions. It does not register content.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
