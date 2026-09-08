package net.minecraft.world.level.block;
import net.minecraft.world.level.block.state.BlockState;
public record Block(String name) {
    public BlockState defaultBlockState() { return new BlockState(name); }
}
