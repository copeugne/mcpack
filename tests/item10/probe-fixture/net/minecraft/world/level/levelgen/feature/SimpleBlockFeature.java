package net.minecraft.world.level.levelgen.feature;
import net.minecraft.world.level.block.state.BlockState;
public class SimpleBlockFeature {
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        context.level().setBlock(context.origin(), new BlockState("urn"), 2);
        return true;
    }
}
