# Cupboard provider contribution

Selector ec856af captures all 18 packaged classes. The 19 generated files
reproduce exactly against independent r1 output. Manifest SHA-256:
f8d8e32b71dd0c3bc4c112b4a11c074563d2368e59b2cfe12ee755bbfb9bd022.

```sh
uv run -m tools.inspect_item8_pool_elements --archive cupboard-1.21-3.7.jar --output evidence/raw/item8/cupboard-provider-r1
```

The common entry registers the event handlers and loads shared configuration.
Server-start and server-tick handlers initialize and poll configuration files;
client hooks provide configuration UI/reload support. Lookup, block-search,
vector and math helpers inspect caller-supplied values or return calculations.
They do not supply a structure, template, feature or authored encounter.

The five mixins provide chunk-load and command/thread diagnostic behavior,
entity-load handling and deferred entity addition. ServerAddEntityMixin queues
off-thread additions and drains them during a later server-thread addEntity call;
it does not introduce a mob-spawn design. Its thread test uses the thread name.
EntityLoadMixin conditionally recovers invalid coordinates or skips an erroring
load, and resets nonfinite rotations. These are existing-entity effects, not
structure generation. Preserve them as compatibility/persistence context;
this scope check does not establish that every optional injection executed.

The complete non-class payload is only metadata, access transformation,
pack metadata and the declared mixin file. No independent structure family.
