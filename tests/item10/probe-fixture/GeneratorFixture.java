import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import org.violetmoon.quark.content.world.gen.MonsterBoxGenerator;
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
                    .invoke(null, (Object) new String[] {"normal"});
            }
            return;
        }
        WorldGenRegion world = new WorldGenRegion();
        world.early = args[0].equals("early");
        world.refuse = args[0].equals("refused");
        world.throwWrite = args[0].equals("exception");
        var generator = new MonsterBoxGenerator();
        var pos = new BlockPos(1, -5, 3);
        try {
            if (args[0].equals("outside")) generator.outside(world, pos);
            else generator.generateChunk(world, null, null, pos);
            System.out.println("completed;arguments=" + world.arguments);
        } catch (IllegalStateException error) {
            System.out.println("exception=" + error.getMessage() + ";arguments=" + world.arguments);
        }
    }
}
