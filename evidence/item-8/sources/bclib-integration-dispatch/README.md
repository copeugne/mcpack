# BCLib integration dispatch for BetterEnd coverage

Selector fedb095 captures BCLib, ModIntegrationAPI and ModIntegration from the
frozen bclib-21.0.24.jar. The complete capture reproduces exactly against fresh
r1 output. Manifest SHA-256:
d085183016dd793119d9f8bbab449fbbc791851dce4ea8244e18da2e9aa4af2c.

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/api/v2/ModIntegrationAPI.class --class-name org/betterx/bclib/integration/ModIntegration.class --class-name org/betterx/bclib/BCLib.class --output evidence/raw/item8/bclib-integration-dispatch-r1
```

ModIntegrationAPI.register stores the supplied integration. registerAll invokes
init only when modIsInstalled returns true; ModIntegration.modIsInstalled
delegates to that integration's ModCore.isLoaded. A separate isDatagen branch
invokes initDatagen. This is a source-level dispatch boundary, not a claim that
registerAll was called at runtime or that datagen ran on the proof server.

For BetterEnd, concrete integrations bind byg, flamboyant and dye_depot through
its captured ModCore declarations. The runtime mod list determines whether
those targets are present. This resolves a direct consumer question without
auditing unrelated BCLib APIs or the absent integrations' geometry. It does not
close the whole BCLib provider row.
