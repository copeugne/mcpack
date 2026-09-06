# WunderLib membership source

Extractor c945125. Independent r1 reproduction matches the manifest and all
three disassemblies byte for byte. Manifest SHA-256:
a9790a69dcedb09289d08c302863b4503d5979fa64942117e17bfa55adb80c5c

```sh
uv run -m tools.inspect_item8_pool_elements --archive wunderlib-21.0.10.jar --class-name de/ambertation/wunderlib/WunderLib.class --class-name de/ambertation/wunderlib/WunderLibClient.class --class-name de/ambertation/wunderlib/math/Bounds.class --output evidence/raw/item8/wunderlib-provider-r1
```

The common entry registers networking payload handlers; the client entry sets
network adapters. Neither registers generation content. Bounds supplies vector
geometry, containment, interpolation, coordinate conversions and serialization.
Its structure-package reference constructs a BoundingBox from supplied extrema.
That reference does not represent structure generation. Full archive accounting
is bound separately by the existing small-utility provider test file.
