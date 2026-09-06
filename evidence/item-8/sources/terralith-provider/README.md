# Terralith provider entry boundaries

Selector 21eac3c captures all eleven classes from the frozen Terralith archive.
The second capture reproduced exactly before this README was added.
Archive SHA-256: d38bd304897731b42f6c013cdc07e082e74411e80c74aabcee385251beb3b546.
Identity manifest SHA-256:
cf0cdfa21a06651e123ae119eadc733c62cc9457fc1131311aac614d5148b1c9.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Terralith_1.21.1_v2.6.2_Neoforge.jar \
  --output evidence/raw/item8/terralith-provider-r1
```

TerralithNeoforge loads ConfigHandler from the loader configuration directory
and attaches RegisterEvent. Its callback registers only the terralith:config
condition codec. TerralithNeoforgeClient installs the configuration screen.
The remaining classes implement configuration state, serialization, the screen
and list entries, identifiers and logging. These classes do not implement a
separate authored generator. The declared mixin list is empty.

ConfigResourceCondition.test returns config.test(key) != invert. The codec's
default invert is false. ConfigState delegates keys to its Modules record;
ConfigHandler loads and saves that state. The packaged NeoForge overlays use
this condition. Their disposition must use the frozen configuration rather
than assuming that all packaged overlay resources are active.

This capture closes the executable entry inspection, not the complete provider
row. Packaged roots, disconnected components, features, functions and overlays
still require their data reconciliation. Preserve that distinction until the
provider scope check is delivered.
