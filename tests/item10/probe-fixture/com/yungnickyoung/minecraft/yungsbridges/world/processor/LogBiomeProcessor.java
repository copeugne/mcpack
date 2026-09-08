package com.yungnickyoung.minecraft.yungsbridges.world.processor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public class LogBiomeProcessor implements ITemplateFeatureProcessor {
    public void process(WorldGenLevel world, BlockPos pos) {
        support(world, pos);
        world.setBlock(pos, new BlockState("air"), 2);
    }
}
