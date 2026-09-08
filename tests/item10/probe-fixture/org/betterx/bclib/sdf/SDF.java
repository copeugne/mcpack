package org.betterx.bclib.sdf;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import org.betterx.bclib.util.BlocksHelper;
public class SDF {
    public void fillRecursive(ServerLevelAccessor world, BlockPos pos) {
        BlocksHelper.setWithoutUpdate(world, pos, new BlockState("pillar"));
        BlocksHelper.setWithoutUpdate(world, new BlockPos(pos.getX(), pos.getY()+1, pos.getZ()), new BlockState("support"));
    }
}
