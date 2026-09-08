import net.minecraft.core.BlockPos;
import net.minecraft.world.level.levelgen.feature.Feature;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
public class DirectFixture {
    public static void main(String[] args) throws Exception {
        if (args[1].equals("isolated")) {
            var location = DirectFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) {
                loader.loadClass("DirectFixture").getMethod("main", String[].class)
                    .invoke(null, (Object) new String[] {args[0], "normal"});
            }
            return;
        }
        TemplateFixture.World world = new TemplateFixture.World();
        world.throwOnThird = args[1].equals("exception");
        world.refuse = args[1].equals("refused");
        var context = new FeaturePlaceContext(world, new BlockPos(1, -5, 3), args[1].equals("early"));
        try {
            boolean returned = false;
            if (args[1].equals("outside")) new Feature().outside(context);
            else if (args[0].equals("anomaly")) returned = new biomesoplenty.worldgen.feature.misc.AnomalyFeature().place(context);
            else returned = new biomesoplenty.worldgen.feature.misc.MonolithFeature().place(context);
            System.out.println("returned=" + returned + ";calls=" + world.calls + ";arguments=" + world.arguments);
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage() + ";calls=" + world.calls + ";arguments=" + world.arguments);
        }
    }
}
