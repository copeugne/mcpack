package org.violetmoon.quark.content.world.gen;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.block.state.BlockState;
public class ObsidianSpikeGenerator {
    public static void placeSpikeAt(WorldGenRegion world, BlockPos pos, RandomSource random) {
        if (world.early) return;
        world.setBlock(pos, new BlockState("obsidian1"), 0);
        world.setBlock(pos, new BlockState("obsidian2"), 0);
        world.setBlock(pos, new BlockState("obsidian3"), 0);
        world.setBlock(pos, new BlockState("obsidian4"), 0);
        world.setBlock(pos, new BlockState("glowstone"), 0);
        world.setBlock(pos, new BlockState("spawner"), 0);
        world.setBlock(pos, new BlockState("chest"), 0);
    }
    public static void outside(WorldGenRegion world, BlockPos pos) {
        world.setBlock(pos, new BlockState("outside"), 0);
    }
}
