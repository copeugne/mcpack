# create-dragons-plus-startup

Extractor 00c6a943f0e3bde95118d5809decea68e78a57f0. Independent r1 reproduction
matches all three disassemblies and the identity manifest. Manifest SHA-256:
abf6643ffff8cb152e132dee8bc25332c43fc684352d193e38559fe3e7356c7b

```sh
uv run -m tools.inspect_item8_pool_elements --archive CreateDragonsPlus-1.11.2b.jar --class-name plus/dragons/createdragonsplus/common/registry/CDPBlockFreezers.class --class-name plus/dragons/createdragonsplus/integration/CDPCompatFix.class --class-name plus/dragons/createdragonsplus/integration/CDPIntegrationContributions.class --output evidence/raw/item8/create-dragons-plus-startup-r1
```

CDPBlockFreezers installs an existing-block processing provider.
CDPCompatFix conditionally registers an Immersive Engineering fluid-hatch
compatibility hook. CDPIntegrationContributions holds consumer dye/fan-processing
callbacks. These are machine processing and integration boundaries, not
independent generated family definitions.

Bind the full parent and nested payload in the provider closure before
changing the provider count. Preserve consumer gameplay effects.
