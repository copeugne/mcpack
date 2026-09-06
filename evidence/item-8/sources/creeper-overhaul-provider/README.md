# Creeper Overhaul provider entries

Extractor aa2c76bca00b2e53d9a751b73ea4cdfb5a4ca3e0. Manifest SHA-256:
f44ec77d75bb58eed2f2475aa44575ca4f894ee557f6ee83549a6efee6844b7c.
Independent r1 matches every generated file.

Retains loader, registry, plugin and common-hook mechanisms for membership review.
Source coverage alone does not close the provider.

```sh
uv run -m tools.inspect_item8_pool_elements --archive CreeperOverhaul-neoforge-1.21.1-4.0.6.jar --class-name tech/thatgravyboat/creeperoverhaul/Creepers.class --class-name tech/thatgravyboat/creeperoverhaul/forge/CreepersForge.class --class-name 'tech/thatgravyboat/creeperoverhaul/forge/CreepersForge$1.class' --class-name tech/thatgravyboat/creeperoverhaul/api/CreeperPlugin.class --class-name tech/thatgravyboat/creeperoverhaul/api/PluginRegistry.class --class-name tech/thatgravyboat/creeperoverhaul/common/registry/ModSpawns.class --class-name tech/thatgravyboat/creeperoverhaul/common/registry/ModEntities.class --class-name tech/thatgravyboat/creeperoverhaul/common/registry/ModBlocks.class --class-name tech/thatgravyboat/creeperoverhaul/common/utils/Events.class --class-name tech/thatgravyboat/creeperoverhaul/common/utils/neoforge/PlatformUtilsImpl.class --class-name tech/thatgravyboat/creeperoverhaul/mixin/IronGolemMixin.class --class-name tech/thatgravyboat/creeperoverhaul/mixin/PlayerListMixin.class --class-name architectury_inject_CreeperOverhaul_common_631d2b68f9d942ccb91d19c357dc7698_5074e7e37c9218544d6a3bdd6fab054dc5791d81201e6912c6e22aba8f3601e3CreeperOverhaul406devjar/PlatformMethods.class --output evidence/raw/item8/creeper-overhaul-provider-r1
```
