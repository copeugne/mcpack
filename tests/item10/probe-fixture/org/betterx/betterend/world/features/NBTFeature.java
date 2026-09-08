package org.betterx.betterend.world.features;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
public class NBTFeature {
    public static BuildingListFeature.StructureInfo selected = new BuildingListFeature.StructureInfo("original.nbt");
    public static StructurePlaceSettings settings = new StructurePlaceSettings();
    public boolean place(FeaturePlaceContext context) {
        if (context.early()) return false;
        StructureTemplate template = selected.getStructure();
        selected = new BuildingListFeature.StructureInfo("later-selection.nbt");
        template.placeInWorld((ServerLevelAccessor) context.level(), context.origin(), context.origin(), settings, null, 4);
        return true;
    }
}
