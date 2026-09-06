# C2ME startup delegates: c2me-notickvd-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
7fdfa69329142dbd1d7a2802d814b2e3fcab3dc33316a7c297c09fdb04402ded

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-notickvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/notickvd/common/Config.class --class-name com/ishland/c2me/notickvd/common/ServerExtNetworking.class --output evidence/raw/item8/c2me-notickvd-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration reads no-tick view-distance settings. The server callback extracts the incoming render distance and sets the listener render-distance override. It does not place or register structure content.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
