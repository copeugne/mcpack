# Bundled Tiny Config entry behavior

Extractor revision 0b01353. Parent: the retained Village Taverns JAR, SHA-256
0e8e3ea2a99c272cbcbb74a117e473f1df35b8929be96c506bf3b39bdd1f3b90.
Nested member: META-INF/jars/tiny-config-3.1.0-neoforge.jar, SHA-256
1587ed9848881e7b677da5b8c85e0f35719315eb5f6571592d31840cf1421f63.
Identity manifest SHA-256:
2216641e92ad3eaa90d728beae2fb5fd0d50f87b271166fdbea1e2adf0bd209a.

```sh
uv run -m tools.inspect_item8_pool_elements --archive village_taverns-neoforge-1.1.5+1.21.1.jar --nested-archive META-INF/jars/tiny-config-3.1.0-neoforge.jar --class-name net/tiny_config/neoforge/ExampleModNeoForge.class --class-name net/tiny_config/ExampleMod.class --class-name net/tiny_config/ConfigManager.class --output evidence/raw/item8/tiny-config-entry-pilot
```

The committed capture reproduces the pilot byte for byte. The extractor verifies
both parent and nested hashes, records nested provenance in the existing archive
field, and cleans the temporary classpath. A top-level Chef's Delight capture
also reproduced its existing disassembly unchanged. Scoped Ruff and Basedpyright
pass after line formatting and explicit complexity exceptions in the existing
capture function. No new schema or runtime measurement was introduced.

ExampleModNeoForge's constructor calls ExampleMod.init, whose body immediately
returns. ConfigManager reads and writes JSON configuration, handles schema
versions and may invoke caller-supplied validator/constraint functions. It does
not itself register a world-generation feature or place a template. Caller
callbacks must be attributed to their callers; this source observation is not
an exclusion of arbitrary client-supplied callback behavior.

Continue the Village Taverns full-payload/entry reconciliation using these
captures and the already captured caller. This source increment does not by
itself close the whole provider or count the bundled library as an additional
retained top-level mod.
