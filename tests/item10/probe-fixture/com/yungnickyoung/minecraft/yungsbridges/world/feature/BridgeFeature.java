package com.yungnickyoung.minecraft.yungsbridges.world.feature;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
public class BridgeFeature extends AbstractTemplateFeature {
    public boolean outside(FeaturePlaceContext context) {
        return createTemplateWithPlacement("yungsbridges:bridge/wood/17_0", context.level(), null, context.origin(), new StructurePlaceSettings()) != null;
    }
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        return createTemplateWithPlacement("yungsbridges:bridge/wood/17_0", context.level(),
            null, context.origin(), new StructurePlaceSettings()) != null;
    }
}
