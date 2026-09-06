# Prickle common initialization

Extractor e852cce1. Independent r1 reproduction matches the manifest and source
byte for byte. Manifest SHA-256:
44697e75f75482b14fbef985cc910ebecf26fd0e15fbdbbcc2b829bb54a5f3d6

```sh
uv run -m tools.inspect_item8_pool_elements --archive prickle-neoforge-1.21.1-21.1.11.jar --class-name net/darkhax/pricklemc/common/impl/PrickleMod.class --output evidence/raw/item8/prickle-init-r1
```

Initialization rejects a repeated call, checks the existing platform service
is available and sets its initialized flag. It registers no world content.
