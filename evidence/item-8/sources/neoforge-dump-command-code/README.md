# Existing registry export capability

Extractor extension `34fccaa` preserves the frozen NeoForge DumpCommand.
Archive SHA: `63ba902edcae4476d49ffc28b18d566b0fcc5bf12edebcce1a2033f254f28155`.
Manifest SHA: `fa8eff257d4a41da1edf9a092326af303160207c616ec4266c750a35a5d244d5`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive neoforge-21.1.249-universal.jar --class-name net/neoforged/neoforge/server/command/DumpCommand.class --output evidence/item-8/sources/neoforge-dump-command-code
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Extraction and scoped checks passed. Reproduce into a fresh directory.
`register` exposes `dump registry`, with alphabetical_sort and print_numeric_ids
boolean arguments. `dumpRegistry` obtains sorted registry keys, writes each
ResourceLocation string, and optionally prefixes its numeric registry ID.
It does not serialize registry values or per-dimension biome-source contents.
Changing the two booleans cannot recover that missing information. The existing
Item 8 registry capture remains valid key enumeration; rerunning it unchanged
would not close dimension eligibility.

This source evidence supports the collection-method decision in
`../lithostitched-biome-injector-code/README.md`. It does not claim that every
other command or runtime inspection route has been exhausted.
