# CTOV provider entry and component code

Twelve packaged classes captured with extractor 61663b4. Independent extraction
reproduced all files byte for byte before this README. Manifest SHA-256:
892790797564491473c7bf42d1e92f182cdb640721aa5e00c9a9b9c044de489e.
Archive SHA-256: 4815b19b83541f09cba556e222612bc5ddcc31f7c4ba2198f4b4d6376cca8b2e.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive '[Neoforge]ctov-3.6.3.jar' \
  --output evidence/raw/item8/ctov-provider-r1
```

The NeoForge constructor registers the common configuration, its server event
listener and the modular compatibility processor. Common init is empty.
ServerAboutToStartEvent invokes CTOV.registerstructure, which subscribes a
Lithostitched AddWorldgenModifiersEvent callback. Verbose bootstrap bindings
preserve this callback and the four root-name construction patterns.

The callback obtains existing vanilla outpost/village structure sets and the
structure registry. Enabled size flags, village names and weights are read from
the NeoForge config through captured platform wrappers. The outpost loop uses
its own eleven-name list, not enabledpillageroutpost. CTOVStructureHelper resolves
the corresponding ctov root with getOrThrow and adds a weighted selection entry
to the supplied set. This modifies eligibility of existing roots; it does not
define a new structure family. Frozen configuration and runtime selection must
still be reconciled with this path rather than inferred from config labels.

CTOVConfigHelper.enabledpillageroutpost calls an array-returning implementation
descriptor, while the captured implementation declares a List return. The
captured startup callback does not invoke that wrapper, so this is a retained
source-level mismatch, not a reproduced runtime failure or a reason to modify
the baseline. Config loading/reloading handlers contain no generation action.

ModularCompatProcessor returns the incoming block when its target mod is absent.
When present, it looks up the configured processor list and applies its processors
in order, stopping when a block result becomes null. An absent list preserves the
incoming block. PlatformHelper resolves mod presence through NeoForge ModList;
TextUtils constructs resource IDs and messages. WorldgenRegistry registers only
this processor type. The generated Architectury bridge identifies NeoForge.

Provider coverage remains open for full resource reconciliation: bundled
compatibility directories/ZIP, modifier-driven components outside root graphs,
and explicit dispositions for disconnected and missing components. Reuse this
complete code capture, the packaged catalog and existing CTOV family regressions.
Do not count source classes, processor lists or component templates as families.
