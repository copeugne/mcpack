package biomesoplenty.worldgen.feature.misc;
import net.minecraft.world.level.levelgen.feature.Feature;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.block.state.BlockState;
public class AnomalyFeature extends Feature {
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        for (int i = 0; i < 3; i++) setBlock(context.level(), context.origin(), new BlockState("content"));
        return true;
    }
}
