import net.minecraft.core.BlockPos;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import com.yungnickyoung.minecraft.betterendisland.world.feature.*;
public class IslandFixture {
    public static class World extends net.minecraft.server.level.WorldGenRegion implements ServerLevelAccessor {}
    private static void place(String kind, ServerLevelAccessor world, boolean early) {
        var pos = new BlockPos(11,22,33);
        var context = new FeaturePlaceContext(world, pos, early);
        switch (kind) {
            case "Gateway" -> System.out.println(BetterEndGatewayFeature.place(context));
            case "Podium" -> System.out.println(new BetterEndPodiumFeature().place(context));
            case "SpawnPlatform" -> System.out.println(BetterEndSpawnPlatformFeature.place(world, pos, early));
            case "Spike" -> BetterSpikeFeature.placeSpike(world, null, null,
                new net.minecraft.world.level.levelgen.feature.SpikeFeature.EndSpike(11, early ? -1 : 22,33), true);
            default -> throw new IllegalArgumentException(kind);
        }
    }
    public static void main(String[] args) throws Exception {
        if (args[0].equals("isolated")) {
            var location = IslandFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) { loader.loadClass("IslandFixture").getMethod("main", String[].class)
                .invoke(null, (Object) new String[] {"normal", args[1]}); }
            return;
        }
        if (args[0].equals("lifecycle")) {
            var world = new TemplateFixture.World(); place(args[1], world, false);
            System.out.println(world.arguments); return;
        }
        var world = new World();
        world.refuse = args[0].equals("refused");
        world.throwOnThird = args[0].equals("recover");
        try { place(args[1], world, args[0].equals("early")); }
        catch (IllegalStateException error) { System.out.println(error.getMessage()); }
        if (args[0].equals("recover")) {
            world.throwOnThird = false; place(args[1], world, false);
        }
        System.out.println(world.arguments);
    }
}
