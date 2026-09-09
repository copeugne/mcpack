import java.lang.instrument.Instrumentation;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.HexFormat;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;
import java.util.zip.GZIPInputStream;

/** Query saved-state collision shapes. No actor, transformers, or world writes. */
public final class Item13CollisionProbe {
    public static void agentmain(String output, Instrumentation instrumentation) throws Exception {
        Object server = null;
        for (Class<?> type : instrumentation.getAllLoadedClasses()) {
            if (type.getName().equals("net.neoforged.neoforge.server.ServerLifecycleHooks")) {
                if (server != null) throw new IllegalStateException("Duplicate server lifecycle class");
                server = type.getMethod("getCurrentServer").invoke(null);
            }
        }
        if (server == null) throw new IllegalStateException("No active NeoForge server");
        ClassLoader loader = server.getClass().getClassLoader();
        Path destination = Path.of(output);
        FutureTask<String> query = new FutureTask<>(() -> snapshot(loader,
            destination.resolveSibling("input.json.gz")));
        server.getClass().getMethod("execute", Runnable.class).invoke(server, query);
        Files.writeString(destination, query.get(30, TimeUnit.SECONDS), StandardOpenOption.CREATE_NEW);
    }

    private static Class<?> type(ClassLoader loader, String name) throws ClassNotFoundException {
        return Class.forName(name, true, loader);
    }

    private static int integer(Object value) {
        if (!(value instanceof Number number) || number.doubleValue() != number.intValue())
            throw new IllegalArgumentException("Expected exact integer: " + value);
        return number.intValue();
    }

    private static String snapshot(ClassLoader loader, Path input) throws Exception {
        String inputHash = HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256")
            .digest(Files.readAllBytes(input)));
        String text;
        try (var stream = new GZIPInputStream(Files.newInputStream(input))) {
            text = new String(stream.readAllBytes(), StandardCharsets.UTF_8);
        }
        Class<?> gsonType = type(loader, "com.google.gson.Gson");
        Object gson = gsonType.getConstructor().newInstance();
        Method jsonTree = gsonType.getMethod("toJsonTree", Object.class);
        Method jsonText = gsonType.getMethod("toJson", Object.class);
        Map<?, ?> document = (Map<?, ?>) gsonType.getMethod("fromJson", String.class, Class.class)
            .invoke(gson, text, Object.class);
        List<?> cases = (List<?>) document.get("cases");
        if (cases.size() != 1) throw new IllegalArgumentException("Exactly one saved case required");
        Map<?, ?> saved = (Map<?, ?>) cases.getFirst();
        if (!"minecraft:the_nether".equals(saved.get("dimension")))
            throw new IllegalArgumentException("Pilot supports Nether build height only");
        List<?> bounds = (List<?>) saved.get("bounds");
        int x0 = integer(bounds.get(0)), y0 = integer(bounds.get(1)), z0 = integer(bounds.get(2));
        int nx = integer(bounds.get(3)) - x0 + 1, ny = integer(bounds.get(4)) - y0 + 1;
        int nz = integer(bounds.get(5)) - z0 + 1;
        List<?> cells = (List<?>) saved.get("blocks_yzx");
        if (nx <= 0 || ny <= 0 || nz <= 0 || Math.multiplyExact(Math.multiplyExact(nx, ny), nz)
                != cells.size() || cells.size() > 8500)
            throw new IllegalArgumentException("Invalid or over-budget voxel count");
        Class<?> stateType = type(loader, "net.minecraft.world.level.block.state.BlockState");
        Class<?> stateBase = type(loader,
            "net.minecraft.world.level.block.state.BlockBehaviour$BlockStateBase");
        Class<?> opsType = type(loader, "com.mojang.serialization.DynamicOps");
        Object ops = type(loader, "com.mojang.serialization.JsonOps").getField("INSTANCE").get(null);
        Object codec = stateType.getField("CODEC").get(null);
        Method parse = type(loader, "com.mojang.serialization.Decoder").getMethod("parse", opsType, Object.class);
        Method encode = type(loader, "com.mojang.serialization.Encoder").getMethod("encodeStart", opsType, Object.class);
        Method result = type(loader, "com.mojang.serialization.DataResult").getMethod("result");
        ArrayList<Object> states = new ArrayList<>();
        ArrayList<Boolean> dynamic = new ArrayList<>();
        Method block = stateBase.getMethod("getBlock");
        Method dynamicShape = type(loader, "net.minecraft.world.level.block.Block").getMethod("hasDynamicShape");
        for (Object paletteEntry : (List<?>) saved.get("palette")) {
            Object tree = jsonTree.invoke(gson, paletteEntry);
            Object state = ((Optional<?>) result.invoke(parse.invoke(codec, ops, tree))).orElseThrow();
            Object roundtrip = ((Optional<?>) result.invoke(encode.invoke(codec, ops, state))).orElseThrow();
            if (!tree.equals(roundtrip)) throw new IllegalStateException("Block state codec changed saved state: " + tree);
            states.add(state);
            dynamic.add((Boolean) dynamicShape.invoke(block.invoke(state)));
        }
        Class<?> posType = type(loader, "net.minecraft.core.BlockPos");
        Class<?> vectorType = type(loader, "net.minecraft.core.Vec3i");
        Method px = vectorType.getMethod("getX"), py = vectorType.getMethod("getY"), pz = vectorType.getMethod("getZ");
        Class<?> getterType = type(loader, "net.minecraft.world.level.BlockGetter");
        Method fluid = stateBase.getMethod("getFluidState");
        Object view = Proxy.newProxyInstance(loader, new Class<?>[]{getterType}, (proxy, method, args) -> {
            if (method.getName().equals("getHeight")) return 256;
            if (method.getName().equals("getMinBuildHeight")) return 0;
            if (method.getName().equals("getBlockState") || method.getName().equals("getFluidState")) {
                int x = (Integer) px.invoke(args[0]) - x0, y = (Integer) py.invoke(args[0]) - y0;
                int z = (Integer) pz.invoke(args[0]) - z0;
                if (x < 0 || x >= nx || y < 0 || y >= ny || z < 0 || z >= nz)
                    throw new UnsupportedOperationException("Shape requested position outside saved view");
                Object state = states.get(integer(cells.get((y * nz + z) * nx + x)));
                return method.getName().equals("getBlockState") ? state : fluid.invoke(state);
            }
            if (method.isDefault()) return InvocationHandler.invokeDefault(proxy, method, args);
            throw new UnsupportedOperationException("Unsupported saved-view query: " + method.getName());
        });
        Class<?> contextType = type(loader, "net.minecraft.world.phys.shapes.CollisionContext");
        Object context = contextType.getMethod("empty").invoke(null);
        Method collision = stateBase.getMethod("getCollisionShape", getterType, posType, contextType);
        Method boxes = type(loader, "net.minecraft.world.phys.shapes.VoxelShape").getMethod("toAabbs");
        Class<?> aabbType = type(loader, "net.minecraft.world.phys.AABB");
        ArrayList<List<List<Double>>> shapes = new ArrayList<>();
        ArrayList<Integer> indices = new ArrayList<>();
        ArrayList<Map<String, Object>> unsupported = new ArrayList<>();
        for (int i = 0; i < cells.size(); i++) {
            Object pos = posType.getConstructor(int.class, int.class, int.class)
                .newInstance(x0 + i % nx, y0 + i / (nx * nz), z0 + (i / nx) % nz);
            try {
                Object shape = collision.invoke(states.get(integer(cells.get(i))), view, pos, context);
                ArrayList<List<Double>> values = new ArrayList<>();
                for (Object box : (List<?>) boxes.invoke(shape)) {
                    ArrayList<Double> coordinates = new ArrayList<>();
                    for (String field : List.of("minX", "minY", "minZ", "maxX", "maxY", "maxZ")) {
                        double value = aabbType.getField(field).getDouble(box);
                        if (!Double.isFinite(value)) throw new IllegalStateException("Nonfinite collision bound");
                        coordinates.add(value);
                    }
                    values.add(coordinates);
                }
                int index = shapes.indexOf(values);
                if (index < 0) { index = shapes.size(); shapes.add(values); }
                indices.add(index);
            } catch (InvocationTargetException error) {
                Throwable cause = error.getCause();
                while (cause.getCause() != null) cause = cause.getCause();
                if (!(cause instanceof UnsupportedOperationException)) throw error;
                indices.add(-1);
                unsupported.add(Map.of("index_yzx", i, "reason", cause.toString()));
            }
        }
        LinkedHashMap<String, Object> output = new LinkedHashMap<>();
        output.put("input_sha256", inputHash);
        output.put("context", "CollisionContext.empty; no actor; saved states without neighbor updates");
        output.put("bounds", bounds);
        output.put("palette_dynamic_shape", dynamic);
        output.put("local_aabbs", shapes);
        output.put("shape_indices_yzx", indices);
        output.put("unsupported", unsupported);
        return jsonText.invoke(gson, output) + "\n";
    }
}
