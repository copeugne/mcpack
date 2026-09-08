package org.betterx.betterend.world.features.terrain;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.core.BlockPos;
import org.betterx.bclib.sdf.SDF;
public class FallenPillarFeature {
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        new SDF().fillRecursive((ServerLevelAccessor) context.level(), new BlockPos(11,22,33));
        return true;
    }
}
