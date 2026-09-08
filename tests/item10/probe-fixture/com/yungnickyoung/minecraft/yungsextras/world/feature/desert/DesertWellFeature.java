package com.yungnickyoung.minecraft.yungsextras.world.feature.desert;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
public class DesertWellFeature extends com.yungnickyoung.minecraft.yungsextras.world.feature.AbstractNbtFeature {
    public boolean outside(FeaturePlaceContext context) {
        return createTemplateFromCenterWithPlacement("yungsextras:desert/wells/well_sm", context.level(), null, context.origin(), new StructurePlaceSettings()) != null;
    }
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        return createTemplateFromCenterWithPlacement("yungsextras:desert/wells/well_sm", context.level(),
            null, context.origin(), new StructurePlaceSettings()) != null;
    }
}
