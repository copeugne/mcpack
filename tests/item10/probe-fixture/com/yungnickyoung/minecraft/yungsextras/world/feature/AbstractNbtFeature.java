package com.yungnickyoung.minecraft.yungsextras.world.feature;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.core.BlockPos;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import com.yungnickyoung.minecraft.yungsextras.world.processor.DesertWellProcessor;
public abstract class AbstractNbtFeature {
    protected StructureTemplate createTemplateFromCenterWithPlacement(String path, WorldGenLevel world,
            RandomSource random, BlockPos pos, StructurePlaceSettings settings) {
        var template = new StructureTemplate();
        template.placeInWorld((ServerLevelAccessor) world, pos, pos, settings, random, 2);
        new DesertWellProcessor().process(world, pos);
        return template;
    }
    protected StructureTemplate createTemplateFromCornerWithPlacement(String path, WorldGenLevel world,
            RandomSource random, BlockPos pos, StructurePlaceSettings settings) {
        var template = new StructureTemplate();
        template.placeInWorld((ServerLevelAccessor) world, pos, pos, settings, random, 2);
        new DesertWellProcessor().process(world, pos);
        return template;
    }
}
