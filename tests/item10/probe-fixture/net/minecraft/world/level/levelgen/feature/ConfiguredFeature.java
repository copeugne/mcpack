package net.minecraft.world.level.levelgen.feature;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.chunk.ChunkGenerator;
import net.minecraft.util.RandomSource;
import net.minecraft.core.BlockPos;
public class ConfiguredFeature {
    public String key = "supplementaries:urns_patch";
    public Object feature() { return new RandomPatchFeature(); }
    public boolean place(WorldGenLevel world, ChunkGenerator generator, RandomSource random, BlockPos pos) {
        return ((RandomPatchFeature) feature()).place(new FeaturePlaceContext(world, pos, false));
    }
    public String toString() { return key; }
}
