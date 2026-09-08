package net.minecraft.world.level.levelgen.feature;
import net.minecraft.world.level.LevelWriter;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
public class Feature {
    protected void setBlock(LevelWriter world, BlockPos pos, BlockState state) {
        world.setBlock(pos, state, 3);
    }
    public void outside(FeaturePlaceContext context) {
        setBlock(context.level(), context.origin(), new BlockState("outside"));
    }
}
