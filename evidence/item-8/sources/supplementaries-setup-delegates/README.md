# Supplementaries setup delegates

Extractor 77b2261fb374a17f6c8566a34ab11295392956a8. Manifest SHA-256:
3a14ffe0a11a67a2cb31b7825dce2fe1bdef83b644754f89816a63558144b58a.
Independent r1 matches every generated file.

RegUtils.registerAdditionalPlacements registers item-to-block placement behavior
for pancakes, sticks, blaze rods, gunpowder and the lunch basket. These are item
placement registrations, not a world-generation structure route. CompatHandler
dispatches setup to optional integrations; its capture identifies the concrete
delegates to reconcile against the retained stack, not a completed compatibility
or whole-provider disposition.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/reg/RegUtils.class --class-name net/mehvahdjukaar/supplementaries/integration/CompatHandler.class --output evidence/raw/item8/supplementaries-setup-delegates-r1
```
