package com.yungnickyoung.minecraft.yungsbridges.world.feature;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.core.BlockPos;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import com.yungnickyoung.minecraft.yungsbridges.world.processor.LogBiomeProcessor;
public abstract class AbstractTemplateFeature {
    protected StructureTemplate createTemplateWithPlacement(String path, WorldGenLevel world,
            RandomSource random, BlockPos pos, StructurePlaceSettings settings) {
        var template = new StructureTemplate();
        template.placeInWorld((ServerLevelAccessor) world, pos, pos, settings, random, 2);
        new LogBiomeProcessor().process(world, pos);
        return template;
    }
}
