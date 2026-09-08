package org.violetmoon.quark.content.world.gen;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.util.RandomSource;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.placement.PlacedFeature;
public class FairyRingGenerator {
    public static void spawnFairyRing(WorldGenLevel world, ChunkGenerator generator, BlockPos pos, RandomSource random) {
        if (((WorldGenRegion) world).early) return;
        world.getBlockState(pos);
        world.setBlock(pos, new BlockState("air"), 2);
        world.getBlockState(pos);
        new PlacedFeature().place(world, generator, random, pos);
        BlockState state = world.getBlockState(pos);
        world.setBlock(pos, state, 2);
        world.getBlockState(pos);
        world.getBlockState(pos);
        world.setBlock(pos, new BlockState("ore-center"), 2);
        world.setBlock(pos, new BlockState("ore-neighbor"), 2);
    }
}
