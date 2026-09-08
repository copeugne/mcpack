package com.yungnickyoung.minecraft.betterendisland.world.feature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.util.RandomSource;
public class BetterEndSpawnPlatformFeature {
    public static boolean place(ServerLevelAccessor world, BlockPos pos, boolean destroy) {
        if (destroy) return false;
        return placeTemplate(world, null, pos, "betterendisland:spawn_platform", 2, destroy);
    }
    private static boolean placeTemplate(ServerLevelAccessor world, RandomSource random, BlockPos pos, Object path, int flags, boolean destroy) {
        new StructureTemplate().placeInWorld(world, pos, pos, new StructurePlaceSettings(), random, flags);
        return true;
    }
}
