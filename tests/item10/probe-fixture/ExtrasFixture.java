import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import com.yungnickyoung.minecraft.yungsextras.world.feature.desert.DesertWellFeature;
import com.yungnickyoung.minecraft.yungsextras.world.processor.DesertWellProcessor;
public class ExtrasFixture {
    public static class World extends BridgeFixture.World {}
    public static class ConfiguredBridge extends net.minecraft.world.level.levelgen.feature.ConfiguredFeature {
        @Override public Object feature() { return new DesertWellFeature(); }
        @Override public boolean place(net.minecraft.world.level.WorldGenLevel world,
                net.minecraft.world.level.chunk.ChunkGenerator generator,
                net.minecraft.util.RandomSource random, BlockPos pos) {
            return new DesertWellFeature().place(new FeaturePlaceContext(world, pos, false));
        }
    }
    public static void main(String[] args) throws Exception {
        if (args[0].equals("isolated")) {
            var location = ExtrasFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) { loader.loadClass("ExtrasFixture").getMethod("main", String[].class)
                .invoke(null, (Object) new String[] {"normal"}); }
            return;
        }
        World world = new World();
        world.refuseAll = args[0].equals("refused");
        world.failProcessor = args[0].equals("exception") || args[0].equals("recover");
        world.throwOnThird = args[0].equals("template-recover");
        try {
            if (args[0].equals("configured")) {
                var configured = new ConfiguredBridge();
                configured.key = "yungsextras:desert/wells/desert_well_sm";
                var context = new net.minecraft.world.level.levelgen.placement.PlacementContext(world, null, java.util.Optional.empty());
                System.out.println("returned=" + net.minecraft.world.level.levelgen.placement.PlacedFeature.lambda$placeWithContext$4(configured, context, null, null, new BlockPos(1, 2, 3)));
            }
            else if (args[0].equals("outside")) new DesertWellProcessor().process(world, new BlockPos(1, 2, 3));
            else if (args[0].equals("outside-template")) System.out.println("returned=" + new DesertWellFeature().outside(new FeaturePlaceContext(world, new BlockPos(1, 2, 3), false)));
            else System.out.println("returned=" + new DesertWellFeature().place(new FeaturePlaceContext(world, new BlockPos(1, 2, 3), args[0].equals("early"))));
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage());
            if (args[0].equals("recover")) System.out.println("same=" + (error == world.failure));
        }
        if (args[0].endsWith("recover")) {
            world.failProcessor = false;
            world.throwOnThird = false;
            System.out.println("recovered=" + new DesertWellFeature().place(new FeaturePlaceContext(world, new BlockPos(4, 5, 6), false)));
        }
        System.out.println(world.arguments);
    }
}
