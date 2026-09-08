import com.tristankechlo.explorations.worldgen.features.ScarecrowFeature;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
public class ProbeFixture {
    public record Dimension(String location) {}
    public static class World implements WorldGenLevel {
        public int calls;
        public boolean throwOnThird;
        public World getLevel() { return this; }
        public Dimension dimension() { return new Dimension("test:dimension"); }
        public boolean setBlock(BlockPos pos, BlockState state, int flags) {
            calls++;
            if (throwOnThird && calls == 3) throw new IllegalStateException("fixture failure");
            return calls != 2;
        }
    }
    public static void main(String[] args) throws Exception {
        if (args[0].equals("transform")) {
            java.nio.file.Files.write(java.nio.file.Path.of(args[2]),
                Item10PlacementProbe.instrument(java.nio.file.Files.readAllBytes(
                    java.nio.file.Path.of(args[1]))));
            return;
        }
        World world = new World();
        world.throwOnThird = args[0].equals("exception");
        try {
            boolean returned = new ScarecrowFeature().place(new FeaturePlaceContext(
                world, new BlockPos(1, -5, 3), args[0].equals("early")));
            System.out.println("returned=" + returned + ";calls=" + world.calls);
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage() + ";calls=" + world.calls);
        }
    }
}
