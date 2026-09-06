# Better Combat team compatibility initialization

Extractor 3b2873c0. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
ece6a78c110821304a3fabfc806c5d7885f8f42612a9c09af83a1f8d47bbdfbf

```sh
uv run -m tools.inspect_item8_pool_elements --archive bettercombat-neoforge-2.3.2+1.21.1.jar --class-name net/bettercombat/compat/FTBTeamsCompat.class --output evidence/raw/item8/better-combat-team-compat-r1
```

Initialization conditionally registers an FTB team relation matcher. It does not
register independent generated content. Preserve its targeting role; no generic
team or platform-loader tracing is required for family membership.
