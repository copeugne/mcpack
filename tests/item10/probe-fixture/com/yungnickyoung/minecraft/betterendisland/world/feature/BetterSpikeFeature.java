package com.yungnickyoung.minecraft.betterendisland.world.feature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.util.RandomSource;
public class BetterSpikeFeature {
    public static void placeSpike(ServerLevelAccessor world, RandomSource random,
        net.minecraft.world.level.levelgen.feature.configurations.SpikeConfiguration config,
        net.minecraft.world.level.levelgen.feature.SpikeFeature.EndSpike spike, boolean worldgen) {
        if (spike.getHeight() < 0) return;
        BlockPos pos = new BlockPos(spike.getCenterX(), spike.getHeight(), spike.getCenterZ());
        placeTemplate(world, random, pos, null, "betterendisland:pillar_initial_1", 2);
        placeTemplate(world, random, pos, null, "betterendisland:pillar_bottom_1", 2);
        world.setBlock(pos, new BlockState("gateway"), 3);
    }
    private static boolean placeTemplate(ServerLevelAccessor world, RandomSource random, BlockPos pos, Object rotation, Object path, int flags) {
        new StructureTemplate().placeInWorld(world, pos, pos, new StructurePlaceSettings(), random, flags);
        return true;
    }
}
