package org.violetmoon.quark.content.world.gen;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.block.state.BlockState;
public class MonsterBoxGenerator {
    public void generateChunk(WorldGenRegion world, ChunkGenerator generator, RandomSource random, BlockPos pos) {
        if (world.early) return;
        world.setBlock(pos, new BlockState("monster_box"), 0);
    }
    public void outside(WorldGenRegion world, BlockPos pos) {
        world.setBlock(pos, new BlockState("monster_box"), 0);
    }
}
