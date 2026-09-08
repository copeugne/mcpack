package com.yungnickyoung.minecraft.betterendisland.world.feature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.util.RandomSource;
public class BetterEndPodiumFeature {
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        placeTemplate((ServerLevelAccessor) context.level(), null, context.origin(), null, "betterendisland:tower_initial", 2);
        return true;
    }
    private boolean placeTemplate(ServerLevelAccessor world, RandomSource random, BlockPos pos, Object rotation, Object path, int flags) {
        new StructureTemplate().placeInWorld(world, pos, pos, new StructurePlaceSettings(), random, flags);
        return true;
    }
}
