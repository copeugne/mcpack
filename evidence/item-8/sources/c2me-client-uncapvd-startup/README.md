# C2ME startup delegates: c2me-client-uncapvd-startup

Extractor 45d7749f9d953ab8ca064a11843d3bb612c8a614. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
7a2948f3fd3a949ecda11bf1898c078a6e0faebf35fcc90a5178ba6ae11d8c17

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-client-uncapvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/client/uncapvd/common/ClientExtNetworking.class --class-name com/ishland/c2me/client/uncapvd/common/Config.class --output evidence/raw/item8/c2me-client-uncapvd-startup-r1
```

These are startup membership inputs. Whole-provider closure remains separate.

Configuration reads view-distance settings and derives a memory-based default. The listener registers extended render-distance messaging and sends the configured view distance when the channel is available. This is client configuration/networking, not authored generation.

This closes the startup delegate role for membership. Do not extend it into
a generic networking or configuration correctness audit.
