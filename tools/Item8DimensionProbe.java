import com.sun.tools.attach.VirtualMachine;
import java.lang.instrument.Instrumentation;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Optional;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;

/** Read possible biome IDs on the server thread. No transformers or world writes. */
public final class Item8DimensionProbe {
    public static void main(String[] args) throws Exception {
        if (args.length != 3) {
            throw new IllegalArgumentException("Expected server PID, agent JAR and new output path");
        }
        VirtualMachine vm = VirtualMachine.attach(args[0]);
        try {
            vm.loadAgent(args[1], args[2]);
        } finally {
            vm.detach();
        }
    }

    public static void agentmain(String output, Instrumentation instrumentation) throws Exception {
        Object server = null;
        for (Class<?> type : instrumentation.getAllLoadedClasses()) {
            if (type.getName().equals("net.neoforged.neoforge.server.ServerLifecycleHooks")) {
                if (server != null) {
                    throw new IllegalStateException("More than one server lifecycle class");
                }
                server = type.getMethod("getCurrentServer").invoke(null);
            }
        }
        if (server == null) {
            throw new IllegalStateException("No active NeoForge server");
        }
        Object activeServer = server;
        FutureTask<String> read = new FutureTask<>(() -> snapshot(activeServer));
        server.getClass().getMethod("execute", Runnable.class).invoke(server, read);
        String result = read.get(30, TimeUnit.SECONDS);
        Files.writeString(Path.of(output), result, StandardOpenOption.CREATE_NEW);
    }

    private static Object call(Object receiver, String method) throws Exception {
        return receiver.getClass().getMethod(method).invoke(receiver);
    }

    private static String identifier(Object key) throws Exception {
        String id = call(key, "location").toString();
        if (!id.matches("[a-z0-9_.-]+:[a-z0-9_./-]+")) {
            throw new IllegalStateException("Invalid registry identifier");
        }
        return id;
    }

    private static String snapshot(Object server) throws Exception {
        TreeMap<String, TreeSet<String>> dimensions = new TreeMap<>();
        for (Object level : (Iterable<?>) call(server, "getAllLevels")) {
            String dimension = identifier(call(level, "dimension"));
            Object generator = call(call(level, "getChunkSource"), "getGenerator");
            Object source = call(generator, "getBiomeSource");
            TreeSet<String> biomes = new TreeSet<>();
            // Subclass reflection can resolve unrelated client-only method signatures.
            Class<?> biomeSource = Class.forName("net.minecraft.world.level.biome.BiomeSource",
                false, source.getClass().getClassLoader());
            Collection<?> possible = (Collection<?>) biomeSource.getMethod("possibleBiomes").invoke(source);
            for (Object holder : possible) {
                Object key = ((Optional<?>) call(holder, "unwrapKey")).orElseThrow();
                biomes.add(identifier(key));
            }
            if (biomes.isEmpty() || dimensions.put(dimension, biomes) != null) {
                throw new IllegalStateException("Empty biome set or duplicate dimension: " + dimension);
            }
        }
        if (dimensions.isEmpty()) {
            throw new IllegalStateException("No loaded dimensions");
        }
        ArrayList<String> rows = new ArrayList<>();
        for (var entry : dimensions.entrySet()) {
            rows.add("  \"" + entry.getKey() + "\": [\""
                + String.join("\", \"", entry.getValue()) + "\"]");
        }
        return "{\n" + String.join(",\n", rows) + "\n}\n";
    }
}
