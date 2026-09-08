import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import org.violetmoon.quark.content.world.gen.MonsterBoxGenerator;
import org.violetmoon.quark.content.world.gen.SpiralSpireGenerator;
import org.violetmoon.quark.content.world.gen.ObsidianSpikeGenerator;
public class GeneratorFixture {
    public static void main(String[] args) throws Exception {
        if (args[0].equals("isolated")) {
            var location = GeneratorFixture.class.getProtectionDomain().getCodeSource().getLocation();
            try (var loader = new java.net.URLClassLoader(new java.net.URL[] {location}, null) {
                @Override protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                    if (name.startsWith("Item10PlacementProbe")) throw new ClassNotFoundException(name);
                    return super.loadClass(name, resolve);
                }
            }) {
                loader.loadClass("GeneratorFixture").getMethod("main", String[].class)
                    .invoke(null, (Object) new String[] {"normal", args.length > 1 ? args[1] : "monster"});
            }
            return;
        }
        WorldGenRegion world = new WorldGenRegion();
        world.early = args[0].equals("early");
        world.refuse = args[0].equals("refused");
        boolean spiral = args.length > 1 && args[1].equals("spiral");
        boolean spike = args.length > 1 && args[1].equals("spike");
        world.throwWrite = args[0].equals("exception") && !spike;
        world.throwOnThird = args[0].equals("exception") && spike;
        var generator = new MonsterBoxGenerator();
        var pos = new BlockPos(1, -5, 3);
        try {
            if (spiral) {
                var spire = new SpiralSpireGenerator();
                if (args[0].equals("outside") || args[0].equals("outside-exception")) {
                    world.throwWrite = args[0].equals("outside-exception");
                    spire.makeSpike(world, null, null, pos);
                } else {
                    spire.generateChunkPart(pos, null, null, new BlockPos(16, 0, 16), world);
                    spire.generateChunkPart(pos, null, null, new BlockPos(32, 0, 16), world);
                    spire.generateChunkPart(new BlockPos(64, 0, 64), null, null, new BlockPos(48, 0, 16), world);
                }
            } else if (spike) {
                if (args[0].equals("outside")) ObsidianSpikeGenerator.outside(world, pos);
                else ObsidianSpikeGenerator.placeSpikeAt(world, pos, null);
            } else if (args[0].equals("outside")) generator.outside(world, pos);
            else generator.generateChunk(world, null, null, pos);
            System.out.println("completed;arguments=" + world.arguments);
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage() + ";arguments=" + world.arguments);
        }
    }
}
