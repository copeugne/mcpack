package org.betterx.bclib.util;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public class BlocksHelper {
    public static void setWithoutUpdate(LevelAccessor world, BlockPos pos, BlockState state) {
        world.setBlock(pos, state, 18);
    }
    public static void setWithoutUpdate(LevelAccessor world, BlockPos pos, net.minecraft.world.level.block.Block block) {
        world.setBlock(pos, block.defaultBlockState(), 18);
    }
}
