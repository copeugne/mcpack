import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import org.betterx.betterend.world.features.NBTFeature;
public class TemplateFixture {
    public static class World extends ProbeFixture.World implements ServerLevelAccessor {
        public boolean refuse;
        public final java.util.List<String> arguments = new java.util.ArrayList<>();
        @Override public boolean setBlock(BlockPos pos, BlockState state, int flags) {
            arguments.add(pos + ";" + state + ";" + flags);
            boolean value = super.setBlock(pos, state, flags);
            return !(refuse && state.name().equals("content")) && value;
        }
    }
    public static void main(String[] args) throws Exception {
        if (args[0].equals("transform")) {
            java.nio.file.Files.write(java.nio.file.Path.of(args[3]),
                Item10PlacementProbe.instrument(args[1], java.nio.file.Files.readAllBytes(java.nio.file.Path.of(args[2]))));
            return;
        }
        if (args[0].equals("isolated")) {
            var location = TemplateFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) {
                loader.loadClass("TemplateFixture").getMethod("main", String[].class)
                    .invoke(null, (Object) new String[] {"normal"});
            }
            return;
        }
        World world = new World();
        world.throwOnThird = args[0].equals("exception");
        world.refuse = args[0].equals("refused");
        NBTFeature.settings.empty = args[0].equals("empty");
        BlockPos pos = new BlockPos(1, -5, 3);
        try {
            boolean returned = args[0].equals("outside")
                ? new net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate()
                    .placeInWorld(world, pos, pos, NBTFeature.settings, null, 4)
                : new NBTFeature().place(new FeaturePlaceContext(world, pos, args[0].equals("early")));
            System.out.println("returned=" + returned + ";calls=" + world.calls + ";arguments=" + world.arguments);
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage() + ";calls=" + world.calls + ";arguments=" + world.arguments);
        }
    }
}
