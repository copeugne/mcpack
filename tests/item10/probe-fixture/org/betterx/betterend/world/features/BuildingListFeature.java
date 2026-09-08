package org.betterx.betterend.world.features;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
public class BuildingListFeature {
    public static class StructureInfo {
        public final String structurePath;
        private final StructureTemplate structure = new StructureTemplate();
        public StructureInfo(String path) { structurePath = path; }
        public StructureTemplate getStructure() { return structure; }
    }
}
