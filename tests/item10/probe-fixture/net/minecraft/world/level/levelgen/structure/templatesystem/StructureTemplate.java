package net.minecraft.world.level.levelgen.structure.templatesystem;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.core.BlockPos;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.block.state.BlockState;
public class StructureTemplate {
    public boolean placeInWorld(ServerLevelAccessor world, BlockPos pos, BlockPos pivot,
                                StructurePlaceSettings settings, RandomSource random, int flags) {
        if (settings.empty) return true;
        world.setBlock(pos, new BlockState("barrier"), flags);
        for (int i = 0; i < 2; i++) world.setBlock(pos, new BlockState("content"), flags);
        world.setBlock(pos, new BlockState("update"), flags);
        return true;
    }
}
