package net.minecraft.world.level.levelgen.placement;
import java.util.Optional;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.chunk.ChunkGenerator;
public record PlacementContext(WorldGenLevel getLevel, ChunkGenerator generator, Optional<PlacedFeature> topFeature) {}
