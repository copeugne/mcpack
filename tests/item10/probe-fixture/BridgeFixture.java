import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import com.yungnickyoung.minecraft.yungsbridges.world.feature.BridgeFeature;
import com.yungnickyoung.minecraft.yungsbridges.world.processor.LogBiomeProcessor;
public class BridgeFixture {
    public static class World extends TemplateFixture.World {
        public boolean failProcessor, refuseAll;
        @Override public boolean setBlock(BlockPos pos, BlockState state, int flags) {
            boolean result = super.setBlock(pos, state, flags);
            if (failProcessor && state.name().equals("support")) throw new IllegalStateException("processor failure");
            return result && !refuseAll;
        }
    }
    public static void main(String[] args) throws Exception {
        if (args[0].equals("isolated")) {
            var location = BridgeFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) { loader.loadClass("BridgeFixture").getMethod("main", String[].class)
                .invoke(null, (Object) new String[] {"normal"}); }
            return;
        }
        World world = new World();
        world.refuseAll = args[0].equals("refused");
        world.failProcessor = args[0].equals("exception");
        try {
            if (args[0].equals("outside")) new LogBiomeProcessor().process(world, new BlockPos(1, 2, 3));
            else if (args[0].equals("outside-template")) System.out.println("returned=" + new BridgeFeature().outside(new FeaturePlaceContext(world, new BlockPos(1, 2, 3), false)));
            else System.out.println("returned=" + new BridgeFeature().place(new FeaturePlaceContext(world, new BlockPos(1, 2, 3), args[0].equals("early"))));
        } catch (IllegalStateException error) { System.out.println("exception=" + error.getMessage()); }
        System.out.println(world.arguments);
    }
}
