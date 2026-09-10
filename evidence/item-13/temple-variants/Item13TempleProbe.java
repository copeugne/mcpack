import java.lang.instrument.Instrumentation;
import java.lang.reflect.Method;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;

/** Declared temple placements or one Basalt central-material placement. */
public final class Item13TempleProbe {
    private static final String BASALT = "adorabuild_structures:basalt_chambers/ancient_debris";
    private static Class<?> type(ClassLoader loader, String name) throws Exception {
        return Class.forName(name, true, loader);
    }

    public static void agentmain(String output, Instrumentation instrumentation) throws Exception {
        Object found = null;
        for (Class<?> cls : instrumentation.getAllLoadedClasses()) {
            if (cls.getName().equals("net.neoforged.neoforge.server.ServerLifecycleHooks")) {
                if (found != null) throw new IllegalStateException("Duplicate lifecycle class");
                found = cls.getMethod("getCurrentServer").invoke(null);
            }
        }
        if (found == null) throw new IllegalStateException("No active server");
        final Object server = found;
        ClassLoader loader = server.getClass().getClassLoader();
        Class<?> gsonType = type(loader,"com.google.gson.Gson");
        Object gson = gsonType.getConstructor().newInstance();
        Path destination = Path.of(output);
        String selection = Files.readString(destination.resolveSibling("selection.json"));
        Map<?,?> plan = (Map<?,?>) gsonType.getMethod("fromJson",String.class,Class.class)
            .invoke(gson,selection,Object.class);
        List<?> selected = (List<?>) plan.get("selected");
        boolean overworld = selected.size() == 1
            && ((Map<?,?>)selected.get(0)).containsKey("structure");
        boolean basalt = selected.size() == 1
            && BASALT.equals(((Map<?,?>)selected.get(0)).get("template"));
        if (!overworld && !basalt && selected.size() != 4)
            throw new IllegalArgumentException("Four temple cases or one Basalt case required");
        if (!basalt && selected.stream().anyMatch(e -> BASALT.equals(((Map<?,?>)e).get("template"))))
            throw new IllegalArgumentException("Basalt cannot be mixed into the temple suite");
        List<Map<String,Object>> cases = new ArrayList<>();
        Map<String,Object> result = new LinkedHashMap<>();
        result.put("method",overworld
            ? "Forced registered-structure placement; bypasses natural spacing/biome selection; not gameplay"
            : "Forced template placement with registered processor; not natural starts or gameplay");
        result.put("cases",cases);
        result.put("rejection_reason","Incomplete placement experiment");
        try {
            for (Object entry : selected) {
                result.put("attempted_case",entry);
                long deadline = System.nanoTime()+TimeUnit.SECONDS.toNanos(30);
                // Off-thread getChunkFuture queues preparation without main-thread managedBlock.
                List<CompletableFuture<?>> pending = chunks(server,loader,(Map<?,?>)entry);
                CompletableFuture.allOf(pending.toArray(new CompletableFuture<?>[0]))
                    .get(Math.max(1,deadline-System.nanoTime()),TimeUnit.NANOSECONDS);
                FutureTask<Map<String,Object>> query = new FutureTask<>(() -> overworld
                    ? placeStructure(server,loader,(Map<?,?>)entry,destination)
                    : place(server,loader,(Map<?,?>)entry,gson));
                server.getClass().getMethod("execute",Runnable.class).invoke(server,query);
                cases.add(query.get(Math.max(1,deadline-System.nanoTime()),TimeUnit.NANOSECONDS));
                // Only a successful case permits the next declared placement.
            }
            result.put("rejection_reason",null);
        } catch (Exception error) {
            result.put("rejection_reason",error.toString());
            throw error;
        } finally {
            Files.writeString(destination,(String)gsonType.getMethod("toJson",Object.class)
                .invoke(gson,result)+"\n",StandardOpenOption.CREATE_NEW);
        }
    }

    private static List<CompletableFuture<?>> chunks(Object server, ClassLoader loader,
            Map<?,?> input) throws Exception {
        Class<?> key = type(loader,"net.minecraft.resources.ResourceKey");
        Class<?> levelType = type(loader,"net.minecraft.world.level.Level");
        boolean overworld = input.containsKey("structure");
        Object level = server.getClass().getMethod("getLevel",key)
            .invoke(server,levelType.getField(overworld ? "OVERWORLD" : "NETHER").get(null));
        if (level == null) throw new IllegalStateException("Selected dimension missing");
        Object source = level.getClass().getMethod("getChunkSource").invoke(level);
        Class<?> status = type(loader,"net.minecraft.world.level.chunk.status.ChunkStatus");
        Method request = source.getClass().getMethod("getChunkFuture",int.class,int.class,status,boolean.class);
        List<?> origin = (List<?>)input.get("origin");
        int x = ((Number)origin.get(0)).intValue(), z = ((Number)origin.get(2)).intValue();
        if (overworld) {
            List<CompletableFuture<?>> pending = new ArrayList<>();
            for (int cx = Math.floorDiv(x,16)-1; cx <= Math.floorDiv(x,16)+1; cx++)
                for (int cz = Math.floorDiv(z,16)-1; cz <= Math.floorDiv(z,16)+1; cz++)
                    pending.add((CompletableFuture<?>)request.invoke(source,cx,cz,status.getField("FULL").get(null),true));
            return pending;
        }
        int size = switch ((String)input.get("template")) {
            case "adorabuild_structures:blackstone_temple_small_1" -> 7;
            case BASALT -> 7;
            case "adorabuild_structures:nether_temple_medium_1" -> 13;
            default -> throw new IllegalArgumentException("Unexpected template");
        };
        List<CompletableFuture<?>> pending = new ArrayList<>();
        System.out.println("ITEM13_TEMPLE_PHASE request-chunks " + origin);
        for (int cx = Math.floorDiv(x-3,16); cx <= Math.floorDiv(x+size+2,16); cx++)
            for (int cz = Math.floorDiv(z-3,16); cz <= Math.floorDiv(z+size+2,16); cz++)
                pending.add((CompletableFuture<?>)request.invoke(source,cx,cz,status.getField("FULL").get(null),true));
        return pending;
    }

    private static Map<String,Object> place(Object server, ClassLoader loader, Map<?,?> input,
            Object gson) throws Exception {
        long begun = System.nanoTime();
        String root = (String) input.get("template");
        int size = switch (root) {
            case "adorabuild_structures:blackstone_temple_small_1" -> 7;
            case BASALT -> 7;
            case "adorabuild_structures:nether_temple_medium_1" -> 13;
            default -> throw new IllegalArgumentException("Unexpected template");
        };
        boolean basalt = root.equals(BASALT);
        int height = basalt ? 7 : (size == 7 ? 8 : 9);
        String processorId = basalt ? "adorabuild_structures:randomize_ancient_debris"
            : "adorabuild_structures:randomize_gold_block";
        List<?> origin = (List<?>)input.get("origin");
        int x0 = ((Number)origin.get(0)).intValue(), y0 = ((Number)origin.get(1)).intValue();
        int z0 = ((Number)origin.get(2)).intValue();
        if (y0 != 160) throw new IllegalArgumentException("Unexpected elevation");
        Class<?> keyType = type(loader,"net.minecraft.resources.ResourceKey");
        Class<?> levelType = type(loader,"net.minecraft.world.level.Level");
        Object level = server.getClass().getMethod("getLevel",keyType)
            .invoke(server,levelType.getField("NETHER").get(null));
        if (level == null) throw new IllegalStateException("Nether missing");
        Class<?> posType = type(loader,"net.minecraft.core.BlockPos");
        Object pos = posType.getConstructor(int.class,int.class,int.class).newInstance(x0,y0,z0);
        Method blockAt = levelType.getMethod("getBlockState",posType);
        int min = (Integer)levelType.getMethod("getMinBuildHeight").invoke(level);
        int max = (Integer)levelType.getMethod("getMaxBuildHeight").invoke(level);
        if (y0-3 < min || y0+height+2 >= max) throw new IllegalStateException("Out of build limits");
        System.out.println("ITEM13_TEMPLE_PHASE clear-check " + root + " " + origin);
        Class<?> stateType = type(loader,"net.minecraft.world.level.block.state.BlockState");
        Method isAir = stateType.getMethod("isAir");
        for (int y = y0; y < y0+height; y++)
            for (int z = z0; z < z0+size; z++)
                for (int x = x0; x < x0+size; x++) {
                    Object p = posType.getConstructor(int.class,int.class,int.class).newInstance(x,y,z);
                    if (!(Boolean)isAir.invoke(blockAt.invoke(level,p)))
                        throw new IllegalStateException("Occupied template target: "+x+","+y+","+z);
                }
        Class<?> idType = type(loader,"net.minecraft.resources.ResourceLocation");
        Method parseId = idType.getMethod("parse",String.class);
        Object manager = server.getClass().getMethod("getStructureManager").invoke(server);
        Object template = ((Optional<?>)manager.getClass().getMethod("get",idType)
            .invoke(manager,parseId.invoke(null,root))).orElseThrow();
        Object actualSize = template.getClass().getMethod("getSize").invoke(template);
        Class<?> vector = type(loader,"net.minecraft.core.Vec3i");
        if ((Integer)vector.getMethod("getX").invoke(actualSize) != size
                || (Integer)vector.getMethod("getY").invoke(actualSize) != height
                || (Integer)vector.getMethod("getZ").invoke(actualSize) != size)
            throw new IllegalStateException("Template dimensions disagree with packaged source");
        Object access = server.getClass().getMethod("registryAccess").invoke(server);
        Object processorKey = type(loader,"net.minecraft.core.registries.Registries").getField("PROCESSOR_LIST").get(null);
        Object registry = type(loader,"net.minecraft.core.RegistryAccess").getMethod("registryOrThrow",keyType)
            .invoke(access,processorKey);
        Object processorList = type(loader,"net.minecraft.core.Registry").getMethod("get",idType)
            .invoke(registry,parseId.invoke(null,processorId));
        if (processorList == null) throw new IllegalStateException("Processor list missing");
        Class<?> settingsType = type(loader,"net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings");
        Object settings = settingsType.getConstructor().newInstance();
        for (Object processor : (List<?>)processorList.getClass().getMethod("list").invoke(processorList))
            settingsType.getMethod("addProcessor",type(loader,"net.minecraft.world.level.levelgen.structure.templatesystem.StructureProcessor"))
                .invoke(settings,processor);
        Class<?> randomType = type(loader,"net.minecraft.util.RandomSource");
        Object random = randomType.getMethod("create",long.class).invoke(null,42L);
        System.out.println("ITEM13_TEMPLE_PHASE place " + root + " " + origin);
        boolean placed = (Boolean)template.getClass().getMethod("placeInWorld",
            type(loader,"net.minecraft.world.level.ServerLevelAccessor"),posType,posType,settingsType,randomType,int.class)
            .invoke(template,level,pos,pos,settings,random,2);
        if (!placed) throw new IllegalStateException("Template placement returned false");
        Object central = posType.getConstructor(int.class,int.class,int.class)
            .newInstance(x0+size/2,y0+(basalt ? 3 : 4),z0+size/2);
        String expected = (String)input.get("expected_central_material");
        Object centralState = blockAt.invoke(level,central);
        Object block = stateType.getMethod("getBlock").invoke(centralState);
        Object blocks = type(loader,"net.minecraft.core.registries.BuiltInRegistries").getField("BLOCK").get(null);
        String observed = type(loader,"net.minecraft.core.Registry").getMethod("getKey",Object.class).invoke(blocks,block).toString();
        if (!expected.equals(observed)) throw new IllegalStateException("Material mismatch: "+expected+" / "+observed);
        Object codec = stateType.getField("CODEC").get(null);
        Object ops = type(loader,"com.mojang.serialization.JsonOps").getField("INSTANCE").get(null);
        Method encode = type(loader,"com.mojang.serialization.Encoder").getMethod("encodeStart",
            type(loader,"com.mojang.serialization.DynamicOps"),Object.class);
        Method result = type(loader,"com.mojang.serialization.DataResult").getMethod("result");
        Class<?> gsonType = gson.getClass();
        Map<String,Integer> indexes = new LinkedHashMap<>();
        List<Object> palette = new ArrayList<>();
        List<Integer> cells = new ArrayList<>();
        for (int y = y0-3; y <= y0+height+2; y++)
            for (int z = z0-3; z <= z0+size+2; z++)
                for (int x = x0-3; x <= x0+size+2; x++) {
                    Object p = posType.getConstructor(int.class,int.class,int.class).newInstance(x,y,z);
                    Object state = blockAt.invoke(level,p);
                    String identifier = state.toString();
                    if (!indexes.containsKey(identifier)) {
                        Object encoded = ((Optional<?>)result.invoke(encode.invoke(codec,ops,state))).orElseThrow();
                        palette.add(gsonType.getMethod("fromJson",String.class,Class.class).invoke(gson,encoded.toString(),Object.class));
                        indexes.put(identifier,indexes.size());
                    }
                    cells.add(indexes.get(identifier));
                }
        Map<String,Object> row = new LinkedHashMap<>();
        row.put("root",root); row.put("dimension","minecraft:the_nether");
        row.put("origin",origin); row.put("rotation","NONE"); row.put("mirror","NONE");
        row.put("processor",processorId); row.put("flags",2);
        row.put("placement_return",placed); row.put("observed_central_material",observed);
        row.put("envelope",List.of(x0,y0,z0,x0+size-1,y0+height-1,z0+size-1));
        row.put("bounds",List.of(x0-3,y0-3,z0-3,x0+size+2,y0+height+2,z0+size+2));
        row.put("palette",palette); row.put("blocks_yzx",cells);
        System.out.println("ITEM13_TEMPLE_PHASE verified " + root + " " + observed);
        row.put("elapsed_seconds",(System.nanoTime()-begun)/1_000_000_000.0);
        return row;
    }
    /** Same generation/placement sequence as PlaceCommand, retaining the actual start. */
    private static Map<String,Object> placeStructure(Object server, ClassLoader loader,
            Map<?,?> input, Path destination) throws Exception {
        String root = (String)input.get("structure");
        if (!List.of("repurposed_structures:temple_ocean", "repurposed_structures:temple_taiga").contains(root))
            throw new IllegalArgumentException("Undeclared structure");
        List<?> origin = (List<?>)input.get("origin");
        int x = ((Number)origin.get(0)).intValue(), z = ((Number)origin.get(2)).intValue();
        boolean ocean = root.endsWith("_ocean");
        if (x != (ocean ? 48 : 8) || z != (ocean ? 128 : -392)
                || ((Number)origin.get(1)).intValue() != 0)
            throw new IllegalArgumentException("Undeclared origin");
        Class<?> levelType = type(loader,"net.minecraft.world.level.Level");
        Class<?> serverLevel = type(loader,"net.minecraft.server.level.ServerLevel");
        Class<?> keyType = type(loader,"net.minecraft.resources.ResourceKey");
        Object level = server.getClass().getMethod("getLevel",keyType)
            .invoke(server,levelType.getField("OVERWORLD").get(null));
        if (level == null) throw new IllegalStateException("Overworld missing");
        long seed = (Long)serverLevel.getMethod("getSeed").invoke(level);
        if (seed != (ocean ? 42L : 6671238423019257953L))
            throw new IllegalStateException("Wrong source seed");
        Object access = server.getClass().getMethod("registryAccess").invoke(server);
        Class<?> accessType = type(loader,"net.minecraft.core.RegistryAccess");
        Object registryKey = type(loader,"net.minecraft.core.registries.Registries").getField("STRUCTURE").get(null);
        Object registry = accessType.getMethod("registryOrThrow",keyType).invoke(access,registryKey);
        Class<?> idType = type(loader,"net.minecraft.resources.ResourceLocation");
        Object id = idType.getMethod("parse",String.class).invoke(null,root);
        Object structure = type(loader,"net.minecraft.core.Registry").getMethod("get",idType).invoke(registry,id);
        if (structure == null) throw new IllegalStateException("Missing registered structure");
        Object source = serverLevel.getMethod("getChunkSource").invoke(level);
        Object generator = source.getClass().getMethod("getGenerator").invoke(source);
        Class<?> generatorType = type(loader,"net.minecraft.world.level.chunk.ChunkGenerator");
        Object biomes = generatorType.getMethod("getBiomeSource").invoke(generator);
        Object randomState = source.getClass().getMethod("randomState").invoke(source);
        Object manager = serverLevel.getMethod("getStructureManager").invoke(level);
        Class<?> chunkType = type(loader,"net.minecraft.world.level.ChunkPos");
        int cx = Math.floorDiv(x,16), cz = Math.floorDiv(z,16);
        Object chunk = chunkType.getConstructor(int.class,int.class).newInstance(cx,cz);
        Class<?> structureType = type(loader,"net.minecraft.world.level.levelgen.structure.Structure");
        Object start = structureType.getMethod("generate",accessType,generatorType,
            type(loader,"net.minecraft.world.level.biome.BiomeSource"),
            type(loader,"net.minecraft.world.level.levelgen.RandomState"),
            type(loader,"net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplateManager"),
            long.class,chunkType,int.class,type(loader,"net.minecraft.world.level.LevelHeightAccessor"),
            java.util.function.Predicate.class).invoke(structure,access,generator,biomes,randomState,
                manager,seed,chunk,0,level,(java.util.function.Predicate<Object>)(ignored -> true));
        Class<?> startType = type(loader,"net.minecraft.world.level.levelgen.structure.StructureStart");
        if (!(Boolean)startType.getMethod("isValid").invoke(start))
            throw new IllegalStateException("Forced start is invalid");
        Object box = startType.getMethod("getBoundingBox").invoke(start);
        Class<?> boxType = type(loader,"net.minecraft.world.level.levelgen.structure.BoundingBox");
        List<Integer> bounds = new ArrayList<>();
        for (String name : List.of("minX","minY","minZ","maxX","maxY","maxZ"))
            bounds.add((Integer)boxType.getMethod(name).invoke(box));
        for (int axis=0; axis<3; axis++)
            if (bounds.get(axis+3)-bounds.get(axis)+1 > 32)
                throw new IllegalStateException("Envelope exceeds declared size: "+bounds);
        if (bounds.get(0)-3 < (cx-1)*16 || bounds.get(3)+3 > (cx+2)*16-1
                || bounds.get(2)-3 < (cz-1)*16 || bounds.get(5)+3 > (cz+2)*16-1)
            throw new IllegalStateException("Padded envelope escapes declared chunk window: "+bounds);
        int min = (Integer)levelType.getMethod("getMinBuildHeight").invoke(level);
        int max = (Integer)levelType.getMethod("getMaxBuildHeight").invoke(level);
        if (bounds.get(1)-3 < min || bounds.get(4)+3 >= max)
            throw new IllegalStateException("Padded envelope escapes build height");
        Class<?> contextType = type(loader,"net.minecraft.world.level.levelgen.structure.pieces.StructurePieceSerializationContext");
        Object context = contextType.getMethod("fromLevel",serverLevel).invoke(null,level);
        Object tag = startType.getMethod("createTag",contextType,chunkType).invoke(start,context,chunk);
        Path startPath = destination.resolveSibling("forced-start.nbt");
        try (var out = new java.io.DataOutputStream(Files.newOutputStream(startPath,StandardOpenOption.CREATE_NEW))) {
            type(loader,"net.minecraft.nbt.NbtIo").getMethod("write",type(loader,"net.minecraft.nbt.CompoundTag"),java.io.DataOutput.class)
                .invoke(null,tag,out);
        }
        Object structureManager = serverLevel.getMethod("structureManager").invoke(level);
        Object random = levelType.getMethod("getRandom").invoke(level);
        Method place = startType.getMethod("placeInChunk",type(loader,"net.minecraft.world.level.WorldGenLevel"),
            type(loader,"net.minecraft.world.level.StructureManager"),generatorType,
            type(loader,"net.minecraft.util.RandomSource"),boxType,chunkType);
        int placed = 0;
        for (int px=Math.floorDiv(bounds.get(0),16); px<=Math.floorDiv(bounds.get(3),16); px++)
            for (int pz=Math.floorDiv(bounds.get(2),16); pz<=Math.floorDiv(bounds.get(5),16); pz++) {
                Object targetChunk = chunkType.getConstructor(int.class,int.class).newInstance(px,pz);
                Object clip = boxType.getConstructor(int.class,int.class,int.class,int.class,int.class,int.class)
                    .newInstance(px*16,min,pz*16,px*16+15,max,pz*16+15);
                place.invoke(start,level,structureManager,generator,random,clip,targetChunk);
                placed++;
            }
        Map<String,Object> result = new LinkedHashMap<>();
        result.put("root",root); result.put("dimension","minecraft:overworld");
        result.put("seed",Long.toString(seed)); result.put("origin",origin);
        result.put("envelope",bounds); result.put("start_nbt","forced-start.nbt");
        result.put("placed_chunks",placed);
        result.put("method","Registered root forced at selected chunk; natural spacing/biome predicate bypassed");
        System.out.println("ITEM13_TEMPLE_PHASE placed-root "+root+" "+bounds);
        return result;
    }

}
