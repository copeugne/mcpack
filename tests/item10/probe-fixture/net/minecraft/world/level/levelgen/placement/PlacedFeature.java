package net.minecraft.world.level.levelgen.placement;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.util.RandomSource;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public class PlacedFeature {
    public boolean place(WorldGenLevel level, ChunkGenerator generator, RandomSource random, BlockPos pos) {
        WorldGenRegion world = (WorldGenRegion) level;
        if (world.flowerException) throw new IllegalStateException("flower failure");
        world.flowerState = new BlockState(world.flowerAir ? "air" : "flower");
        world.setBlock(pos, world.flowerState, 2);
        return world.flowerReturn;
    }
}
