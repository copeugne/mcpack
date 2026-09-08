package com.yungnickyoung.minecraft.betterendisland.world.feature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.util.RandomSource;
public class BetterEndGatewayFeature {
    public static boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        placeTemplate((ServerLevelAccessor) context.level(), null, context.origin(), "betterendisland:gateway", 2);
        context.level().setBlock(context.origin(), new BlockState("gateway"), 3);
        return true;
    }
    private static boolean placeTemplate(ServerLevelAccessor world, RandomSource random, BlockPos pos, Object path, int flags) {
        new StructureTemplate().placeInWorld(world, pos, pos, new StructurePlaceSettings(), random, flags);
        return true;
    }
}
