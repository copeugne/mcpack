package com.yungnickyoung.minecraft.yungsbridges.world.processor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public interface ITemplateFeatureProcessor {
    default void support(WorldGenLevel world, BlockPos pos) {
        world.setBlock(pos, new BlockState("support"), 2);
        world.setBlock(new BlockPos(1, 0, 1), new BlockState("pillar"), 2);
    }
}
