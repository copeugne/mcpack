package org.violetmoon.quark.content.world.gen;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.world.level.block.state.BlockState;
import java.util.Random;
public class SpiralSpireGenerator {
    public void generateChunkPart(BlockPos source, ChunkGenerator generator, Random random,
                                  BlockPos chunk, WorldGenRegion world) {
        if (world.early) return;
        makeSpike(world, generator, random, chunk);
    }
    public void makeSpike(WorldGenRegion world, ChunkGenerator generator, Random random, BlockPos pos) {
        world.setBlock(pos, new BlockState("spire1"), 0);
        world.setBlock(pos, new BlockState("spire2"), 0);
    }
}
