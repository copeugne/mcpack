# Custom pool codec evidence

This source inspection resolves the packaged-reference fields of the custom
pool element types encountered in the retained catalog. It is not evidence of
successful structure placement or final family coverage.

Reproduce from the repository root with the frozen acquired artifacts and pinned
Temurin installation available:

```sh
uv run -m tools.inspect_item8_pool_elements --output evidence/raw/item8/pool-codecs-reproduction
```

The collector at `3fd012c`, extended with resolver classes at `898e934`, hashes
the retained input archives, selects the observed custom element implementations
and their registration classes, and invokes the
pinned `javap -p -c -constants`. `identities.json` binds each disassembly to its
archive, original class bytes, and output bytes. The delivered output matched the
pilot byte-for-byte using `diff -r`. Directory names preserve their source JAR
names; their contents are text files, not binaries.

YUNG's and Integrated API expose `location` and `processors` codecs directly.
WorldWeaver's End, Illager Invasion's no-liquid, Moog's mirroring, and Repurposed
Structures' ocean-bottom elements inherit single-template handling. Their custom
placement behavior remains distinct. For example, the End element checks height
and air before delegating placement. These classes support tracing template
references, not assuming vanilla placement semantics.

Moog's version-aware element decodes `location` and version-keyed `locations`,
then calls `VersionResolver` to choose a template. The retained resolver contains
the constant `1.21.1`, compares numeric version components with zero padding,
and uses inclusive bounds. The link reader now marks the uniquely matching
mapping as selected and preserves fallback and other-version locations as
unselected. It rejects ambiguous or nonmatching mappings instead of relying on
catalog key order or silently taking a fallback. This intentionally verifies the
observed closed numeric mappings for the frozen identity; it is not a general
replacement for every format the mod might support.

The complete frozen JSON catalog has 212 such versioned elements, each with one
selected mapping. Reproduce that source-bound check with:

```sh
uv run pytest -q tests/item8/test_pool_links.py
```

Do not infer selection from the absence of log messages: selected-template
logging is conditional on the mod's debug flag. The selection here is derived
from preserved bytecode and packaged mappings, not claimed as a logged runtime
observation.

The link reader also preserves inline placed-feature definitions found in the
packaged pools. These can author entities, such as Supplementaries' boat with
passengers, and must not be lost by assuming every feature is a registry ID.
`src/mcpack_evidence/item8_pool_links.py` is the reproducible link extraction logic;
its output preserves source paths, field pointers, optional-pack prefixes,
competing definitions and unresolved types. A potential link is not proof that
geometry, processors, alias selection, generation depth or runtime configuration
will permit that member to appear in an assembled structure.
