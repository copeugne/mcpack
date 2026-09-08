package net.minecraft.world.level.levelgen.feature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.WorldGenLevel;
public record FeaturePlaceContext(WorldGenLevel level, BlockPos origin, boolean early) {}
