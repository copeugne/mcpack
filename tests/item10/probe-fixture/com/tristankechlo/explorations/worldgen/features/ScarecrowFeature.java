package com.tristankechlo.explorations.worldgen.features;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
public class ScarecrowFeature {
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        WorldGenLevel level = context.level();
        BlockPos pos = context.origin();
        BlockState state = new BlockState("test:marker");
        boolean result = level.setBlock(pos, state, 2);
        result &= level.setBlock(pos, state, 2);
        result &= level.setBlock(pos, state, 2);
        result &= level.setBlock(pos, state, 2);
        result &= level.setBlock(pos, state, 2);
        return result;
    }
}
