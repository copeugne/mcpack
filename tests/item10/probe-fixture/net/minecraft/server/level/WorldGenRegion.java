package net.minecraft.server.level;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.block.state.BlockState;
public class WorldGenRegion implements WorldGenLevel {
    public record Dimension(String location) {}
    public boolean early, refuse, throwWrite, throwOnThird;
    public final java.util.List<String> arguments = new java.util.ArrayList<>();
    public WorldGenRegion getLevel() { return this; }
    public Dimension dimension() { return new Dimension("test:dimension"); }
    public boolean setBlock(BlockPos pos, BlockState state, int flags) {
        arguments.add(pos + ";" + state + ";" + flags);
        if (throwWrite || (throwOnThird && arguments.size() == 3)) throw new IllegalStateException("generator fixture failure");
        return !refuse;
    }
}
