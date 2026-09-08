package com.yungnickyoung.minecraft.yungsextras.world.processor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public class DesertWellProcessor {
    public void process(WorldGenLevel world, BlockPos pos) {
        world.setBlock(pos, new BlockState("support"), 2);
        world.setBlock(pos, new BlockState("sand"), 2);
        world.setBlock(pos, new BlockState("suspicious_sand"), 3);
    }
}
