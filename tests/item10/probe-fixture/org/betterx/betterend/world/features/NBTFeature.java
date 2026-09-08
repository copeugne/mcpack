package org.betterx.betterend.world.features;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
public class NBTFeature {
    public static BuildingListFeature.StructureInfo selected = new BuildingListFeature.StructureInfo("original.nbt");
    public static StructurePlaceSettings settings = new StructurePlaceSettings();
    protected net.minecraft.core.BlockPos getGround(net.minecraft.world.level.WorldGenLevel world,
                                                    net.minecraft.core.BlockPos pos) {
        return pos;
    }
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        getGround(context.level(), context.origin());
        StructureTemplate template = selected.getStructure();
        selected = new BuildingListFeature.StructureInfo("later-selection.nbt");
        template.placeInWorld((ServerLevelAccessor) context.level(), context.origin(), context.origin(), settings, null, 4);
        return true;
    }
}
