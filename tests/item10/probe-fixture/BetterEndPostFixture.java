import net.minecraft.core.BlockPos;
import net.minecraft.world.level.levelgen.feature.FeaturePlaceContext;
import org.betterx.betterend.world.features.NBTFeature;
public class BetterEndPostFixture {
    public static void main(String[] args) {
        var world = new BridgeFixture.World();
        world.refuseAll = args[0].equals("refused");
        world.failProcessor = args[0].equals("recover");
        NBTFeature.postWrites = true;
        try {
            System.out.println("returned=" + new NBTFeature().place(new FeaturePlaceContext(world, new BlockPos(1,2,3), false)));
        } catch (IllegalStateException error) { System.out.println("same=" + (error == world.failure)); }
        if (args[0].equals("recover")) {
            world.failProcessor = false;
            System.out.println("recovered=" + new NBTFeature().place(new FeaturePlaceContext(world, new BlockPos(4,5,6), false)));
        }
        System.out.println(world.arguments);
    }
}
