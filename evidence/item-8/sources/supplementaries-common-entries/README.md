# Supplementaries common entries and stronghold hooks

Extractor b0508d13ad94d020a18aa34f6f4ebb3d80a91831. Manifest SHA-256:
7d0fe813b6039a677168e347e9c9d73c4af2aae8d9b2728cab6e9b9783ac2e74.
Independent r1 matches every generated file.

Retains the actual loader, common initialization and server events, mixin selector
and two stronghold component hooks for provider membership interpretation.
Source coverage alone does not close the provider.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/Supplementaries.class --class-name net/mehvahdjukaar/supplementaries/platform/SupplementariesForge.class --class-name net/mehvahdjukaar/supplementaries/common/events/ServerEvents.class --class-name net/mehvahdjukaar/supplementaries/common/events/platform/ServerEventsForge.class --class-name net/mehvahdjukaar/supplementaries/mixins/MixinPlugin.class --class-name net/mehvahdjukaar/supplementaries/mixins/StrongholdCrossingSconceMixin.class --class-name net/mehvahdjukaar/supplementaries/mixins/StrongholdRoomSconceMixin.class --output evidence/raw/item8/supplementaries-common-entries-r1
```
