import net.minecraft.core.BlockPos;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import org.betterx.bclib.sdf.SDF;
public class PillarFixture {
    public static void main(String[] args) throws Exception {
        String mode = args[0];
        if (mode.equals("isolated")) {
            var location = PillarFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) { loader.loadClass("PillarFixture").getMethod("main", String[].class)
                .invoke(null, (Object) new String[] {"normal", args[1]}); }
            return;
        }
        var world = new BridgeFixture.World();
        world.refuseAll = mode.equals("refused");
        world.failProcessor = mode.equals("recover");
        var feature = Class.forName("org.betterx.betterend.world.features.terrain." + args[1]).getConstructor().newInstance();
        var place = feature.getClass().getMethod("place", FeaturePlaceContext.class);
        try {
            if (mode.equals("outside")) new SDF().fillRecursive(world, new BlockPos(4,5,6));
            else System.out.println("returned=" + place.invoke(feature, new FeaturePlaceContext(world, new BlockPos(1,2,3), mode.equals("early"))));
        } catch (java.lang.reflect.InvocationTargetException error) {
            System.out.println("same=" + (error.getCause() == world.failure));
        }
        if (mode.equals("recover")) {
            world.failProcessor = false;
            System.out.println("recovered=" + place.invoke(feature, new FeaturePlaceContext(world, new BlockPos(7,8,9), false)));
        }
        System.out.println(world.arguments);
    }
}
