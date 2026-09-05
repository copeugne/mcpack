# Seven Seas and Towns and Towers wrappers

Extractor revision 2254e9f. Both captures reproduced byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar --output evidence/raw/item8/seven-seas-entry-r1
uv run -m tools.inspect_item8_pool_elements --archive t_and_t-neoforge-fabric-1.13.9+1.21.1.jar --output evidence/raw/item8/towns-towers-entry-r1
```

Identity manifest hashes:

- seven-seas-entry/identities.json:
  b82d3324c4f57e1b0716794726edd9d6320d6b8b4e06994eea806fb6ae69b693.
- towns-towers-entry/identities.json:
  7aed5f9f757223b833f1ea7a9ca7934da30a5b4acf5ae4c296a5648634e3cd7e.

Seven Seas has one class: an empty constructor and logger initialization.
Towns and Towers has three classes: its NeoForge constructor calls common init,
which only logs; the generated platform helper returns neoforge. None of these
classes registers a feature, event callback or direct structure placement.
This accounts for the wrappers' behavior, not their entire resource scope.

Continue packaged root/pool/template reconciliation, including the optional
Towns and Towers Waystones pack and Cristel Lib declarations. Shared consumers
remain attributable separately. Do not infer whole-provider completeness solely
from these empty or logging-only entry implementations.
