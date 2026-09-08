import java.util.Optional;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.placement.PlacedFeature;
import net.minecraft.world.level.levelgen.placement.PlacementContext;
public class UrnFixture {
    public static void main(String[] args) throws Exception {
        if (args[0].equals("isolated")) {
            var location = UrnFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) { loader.loadClass("UrnFixture").getMethod("main", String[].class)
                .invoke(null, (Object) new String[] {"normal"}); }
            return;
        }
        var world = new WorldGenRegion();
        world.refuse = args[0].equals("refused");
        world.throwWrite = args[0].equals("exception");
        var configured = new ConfiguredFeature();
        if (args[0].equals("unrelated")) configured.key = "test:other_patch";
        var parent = new PlacedFeature();
        if (args[0].equals("galleon")) parent.key = "test:galleon_component";
        var context = new PlacementContext(world, null,
            args[0].equals("absent") ? Optional.empty() : Optional.of(parent));
        for (int i = 0; i < 2; i++) {
            try { System.out.println("returned=" + PlacedFeature.lambda$placeWithContext$4(
                configured, context, null, null, new BlockPos(i, 2, 3))); }
            catch (IllegalStateException error) { System.out.println("exception=" + error.getMessage()); }
            world.throwWrite = false;
        }
        System.out.println(world.arguments);
    }
}
