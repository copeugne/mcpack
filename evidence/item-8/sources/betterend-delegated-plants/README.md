# BetterEnd delegated plant placement

Selector eeb52f3 captures the seven concrete growth consumers, their shared
EndPlantWithAgeBlock base and EndBlocks registration binding. The complete
capture reproduces exactly against fresh r1 output. Manifest SHA-256:
2252cf72f8e265ab1b314a98677c758eb0735264a09707e1d5595a8b1e908d16.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/blocks/BlueVineSeedBlock.class --class-name org/betterx/betterend/blocks/EndLilySeedBlock.class --class-name org/betterx/betterend/blocks/EndLotusSeedBlock.class --class-name org/betterx/betterend/blocks/GlowingPillarSeedBlock.class --class-name org/betterx/betterend/blocks/HydraluxSaplingBlock.class --class-name org/betterx/betterend/blocks/LanceleafSeedBlock.class --class-name org/betterx/betterend/blocks/NeonCactusPlantBlock.class --class-name org/betterx/betterend/blocks/basis/EndPlantWithAgeBlock.class --class-name org/betterx/betterend/registry/EndBlocks.class --output evidence/raw/item8/betterend-delegated-plants-r1
```

EndBlocks binds the feature fields to BlueVineSeedBlock, EndLilySeedBlock,
EndLotusSeedBlock, GlowingPillarSeedBlock, HydraluxSaplingBlock, LanceleafSeedBlock
and NeonCactusPlantBlock. Their growth bodies place the respective vegetation:
blue vine/fur/lantern; lily; lotus stem/leaf/flower; glowing-pillar roots/leaves/
luminophor; hydralux; lanceleaf; and cactus. These direct consumers resolve the
features whose placement body delegates to seed/sapling growth. They do not
supply another authored building or encounter family. In particular glowing
pillar is a plant here, distinct from the previously preserved obsidian-pillar
landmark candidates and central-island pillar components. No geometry audit
or broader plant behavior test is needed for this candidate-role distinction.
