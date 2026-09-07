# Ritchie's Projectile Library provider scope source

Selector revision: 0cbba5c. All 34 classes from the retained archive
`ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar` are captured. Archive SHA-256:
`cc509060833736fb650aa4c36b1ce33a7eeeb9ca6e9f8e80a7c951c9e7487b24`.
Identity manifest SHA-256: `7ee4ba1c377fb21900a6a47e8ac3a041ab29128fd250f97bbdb611d4b77656a1`.
Independent extraction reproduces byte for byte.

```sh
uv run -m tools.inspect_item8_pool_elements --archive ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar --output evidence/raw/item8/projectile-library-provider-r1
```

Compare identities.json and the listed disassemblies; this explanatory README
was added after raw comparison. No new runtime or gameplay experiment was needed.

The sole @Mod constructor initializes networking, registers configuration and
player-login/server-level-tick callbacks. The two auto-subscribers register packet
handling and client camera/tick/logout effects. RPLNetwork's packet constructors
cover channel version checking, precise entity motion, screen shaking and burst
subprojectile synchronization. Client handlers operate on those client effects
and existing entities. They do not load authored structure data.

The packaged common mixin implements motion synchronization for tagged entity
types. The packaged Forge mixin list is empty. Neither configuration is declared
in neoforge.mods.toml or the minimal MANIFEST.MF. These are packaged implementation
findings, not proof of activation. No baseline correction is made. The access widener exposes the Projectile
constructor, not a generation entry. Tags are code-defined entity tag keys,
without packaged tag or generation data. Configurations control projectile chunk
loading; saved ChunkManager queues/ticks force-loading requests for supplied
coordinates and manages their lifetime. This can affect which chunks are loaded,
but contributes no new authored layout or structure-family definition.

ProjectileBurst is an abstract entity base with consumer-supplied lifetime, forces
and dimensions. It stores and updates subprojectile positions, performs collision
queries and dispatches hit callbacks. The clip/collision helpers, renderer and
screen-shake classes support that entity behavior. No concrete authored structure
generator, root, pool, feature, template, nested archive or resource loader exists
in this payload. Consumer projectile effects remain consumer behavior; this source
review does not prove their combat balance, safety or chunk-loading performance.
