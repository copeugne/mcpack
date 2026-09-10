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
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;

/** Four declared forced placements, with first-case validation before expansion. */
public final class Item13TempleProbe {
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
        if (selected.size() != 4) throw new IllegalArgumentException("Exactly four cases required");
        List<Map<String,Object>> cases = new ArrayList<>();
        Map<String,Object> result = new LinkedHashMap<>();
        result.put("method","Forced template placement with registered processor; not natural starts or gameplay");
        result.put("cases",cases);
        result.put("rejection_reason","Incomplete placement experiment");
        try {
            for (Object entry : selected) {
                result.put("attempted_case",entry);
                FutureTask<Map<String,Object>> query = new FutureTask<>(() -> place(server,loader,(Map<?,?>)entry,gson));
                server.getClass().getMethod("execute",Runnable.class).invoke(server,query);
                cases.add(query.get(30,TimeUnit.SECONDS));
                // Only a successful, read-back-verified case permits the next placement.
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

    private static Map<String,Object> place(Object server, ClassLoader loader, Map<?,?> input,
            Object gson) throws Exception {
        long begun = System.nanoTime();
        String root = (String) input.get("template");
        int size = switch (root) {
            case "adorabuild_structures:blackstone_temple_small_1" -> 7;
            case "adorabuild_structures:nether_temple_medium_1" -> 13;
            default -> throw new IllegalArgumentException("Unexpected template");
        };
        int height = size == 7 ? 8 : 9;
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
        System.out.println("ITEM13_TEMPLE_PHASE chunks " + root + " " + origin);
        for (int cx = Math.floorDiv(x0-3,16); cx <= Math.floorDiv(x0+size+2,16); cx++)
            for (int cz = Math.floorDiv(z0-3,16); cz <= Math.floorDiv(z0+size+2,16); cz++)
                levelType.getMethod("getChunk",int.class,int.class).invoke(level,cx,cz);
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
            .invoke(registry,parseId.invoke(null,"adorabuild_structures:randomize_gold_block"));
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
            .newInstance(x0+size/2,y0+4,z0+size/2);
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
        row.put("processor","adorabuild_structures:randomize_gold_block"); row.put("flags",2);
        row.put("placement_return",placed); row.put("observed_central_material",observed);
        row.put("envelope",List.of(x0,y0,z0,x0+size-1,y0+height-1,z0+size-1));
        row.put("bounds",List.of(x0-3,y0-3,z0-3,x0+size+2,y0+height+2,z0+size+2));
        row.put("palette",palette); row.put("blocks_yzx",cells);
        System.out.println("ITEM13_TEMPLE_PHASE verified " + root + " " + observed);
        row.put("elapsed_seconds",(System.nanoTime()-begun)/1_000_000_000.0);
        return row;
    }
}
