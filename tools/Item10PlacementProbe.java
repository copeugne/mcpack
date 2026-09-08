import java.lang.instrument.ClassFileTransformer;
import java.lang.instrument.Instrumentation;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.security.ProtectionDomain;
import java.util.HexFormat;
import java.util.IdentityHashMap;
import java.util.Map;
import java.util.Collections;
import java.security.MessageDigest;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import jdk.internal.org.objectweb.asm.ClassReader;
import jdk.internal.org.objectweb.asm.ClassVisitor;
import jdk.internal.org.objectweb.asm.ClassWriter;
import jdk.internal.org.objectweb.asm.MethodVisitor;
import jdk.internal.org.objectweb.asm.Opcodes;

/** Measurement probe: retain targeted feature and template writes without changing their results. */
public final class Item10PlacementProbe {
    private static final String TARGET =
        "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature";
    private static final String WRITE_DESCRIPTOR =
        "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;I)Z";
    private static final AtomicLong SEQUENCE = new AtomicLong();
    private static final ConcurrentHashMap<Long, Long> ACTIVE = new ConcurrentHashMap<>();
    private static final String ANOMALY = "biomesoplenty/worldgen/feature/misc/AnomalyFeature";
    private static final String MONOLITH = "biomesoplenty/worldgen/feature/misc/MonolithFeature";
    private static final String BASE_FEATURE = "net/minecraft/world/level/levelgen/feature/Feature";
    private static final String BASE_WRITE = "(Lnet/minecraft/world/level/LevelWriter;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)V";
    private static final String END_FEATURE = "org/betterx/betterend/world/features/NBTFeature";
    private static final String SHIP = "org/betterx/betterend/world/features/CrashedShipFeature";
    private static final String INFO = "org/betterx/betterend/world/features/BuildingListFeature$StructureInfo";
    private static final String TEMPLATE = "net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplate";
    private static final String TEMPLATE_DESCRIPTOR =
        "(Lnet/minecraft/world/level/ServerLevelAccessor;Lnet/minecraft/core/BlockPos;"
        + "Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/levelgen/structure/templatesystem/StructurePlaceSettings;"
        + "Lnet/minecraft/util/RandomSource;I)Z";
    private static final String TEMPLATE_BRIDGE =
        "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z";
    private static final Map<Object, String> TEMPLATE_PATHS =
        Collections.synchronizedMap(new IdentityHashMap<>());
    private static final ConcurrentHashMap<Long, String> FEATURES = new ConcurrentHashMap<>();
    private static final ConcurrentHashMap<Long, Boolean> IN_TEMPLATE = new ConcurrentHashMap<>();
    private static Path output;
    private static volatile boolean installed;

    private Item10PlacementProbe() {}

    private static String quote(Object value) {
        return "\"" + value.toString().replace("\\", "\\\\").replace("\"", "\\\"")
            .replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t") + "\"";
    }

    private static synchronized void emit(String row) {
        try {
            Files.writeString(output, row + "\n", StandardOpenOption.APPEND);
        } catch (Exception error) {
            throw new IllegalStateException("Placement observation could not be retained", error);
        }
    }

    private static Object call(Object receiver, String name) throws Throwable {
        try {
            return receiver.getClass().getMethod(name).invoke(receiver);
        } catch (InvocationTargetException error) {
            throw error.getCause();
        }
    }

    private static String position(Object pos) throws Throwable {
        return "[" + call(pos, "getX") + "," + call(pos, "getY") + "," + call(pos, "getZ") + "]";
    }

    public static void begin(Object context) throws Throwable {
        long thread = Thread.currentThread().threadId();
        long id = SEQUENCE.incrementAndGet();
        if (ACTIVE.putIfAbsent(thread, id) != null) {
            throw new IllegalStateException("Nested or unfinished scarecrow attempt");
        }
        Object world = call(context, "level");
        Object level = call(world, "getLevel");
        Object dimension = call(call(level, "dimension"), "location");
        emit("{\"kind\":\"begin\",\"attempt\":" + id + ",\"dimension\":"
            + quote(dimension) + ",\"origin\":" + position(call(context, "origin")) + "}");
    }

    public static boolean write(Object world, Object pos, Object state, int flags) throws Throwable {
        Long attempt = ACTIVE.get(Thread.currentThread().threadId());
        if (attempt == null) {
            throw new IllegalStateException("Write outside traced attempt");
        }
        String coordinates = position(pos);
        Method method = Class.forName("net.minecraft.world.level.WorldGenLevel", false,
            world.getClass().getClassLoader()).getMethod("setBlock",
                Class.forName("net.minecraft.core.BlockPos", false, world.getClass().getClassLoader()),
                Class.forName("net.minecraft.world.level.block.state.BlockState", false,
                    world.getClass().getClassLoader()), int.class);
        boolean result;
        try {
            result = (Boolean) method.invoke(world, pos, state, flags);
        } catch (InvocationTargetException error) {
            emit("{\"kind\":\"write_exception\",\"attempt\":" + attempt
                + ",\"position\":" + coordinates + ",\"exception\":"
                + quote(error.getCause().getClass().getName()) + "}");
            throw error.getCause();
        }
        emit("{\"kind\":\"write\",\"attempt\":" + attempt + ",\"position\":"
            + coordinates + ",\"state\":" + quote(state) + ",\"flags\":" + flags
            + ",\"returned\":" + result + "}");
        return result;
    }

    public static void end(boolean returned) {
        FEATURES.remove(Thread.currentThread().threadId());
        Long id = ACTIVE.remove(Thread.currentThread().threadId());
        if (id == null) {
            throw new IllegalStateException("Exit outside traced attempt");
        }
        emit("{\"kind\":\"end\",\"attempt\":" + id + ",\"returned\":" + returned + "}");
    }

    public static void beginFeature(Object feature, Object context) throws Throwable {
        begin(context);
        long thread = Thread.currentThread().threadId();
        FEATURES.put(thread, feature.getClass().getName());
        emit("{\"kind\":\"feature\",\"attempt\":" + ACTIVE.get(thread)
            + ",\"class\":" + quote(feature.getClass().getName()) + "}");
    }

    public static void ground(Object pos) throws Throwable {
        Long attempt = ACTIVE.get(Thread.currentThread().threadId());
        if (attempt == null) throw new IllegalStateException("Ground outside traced attempt");
        emit("{\"kind\":\"ground\",\"attempt\":" + attempt
            + ",\"position\":" + position(pos) + "}");
    }

    public static void selected(Object info, Object template) throws ReflectiveOperationException {
        String path = (String) info.getClass().getField("structurePath").get(info);
        synchronized (TEMPLATE_PATHS) {
            String previous = TEMPLATE_PATHS.putIfAbsent(template, path);
            if (previous != null && !previous.equals(path)) {
                throw new IllegalStateException("One template object has conflicting source paths");
            }
        }
    }

    public static boolean template(Object template, Object world, Object pos, Object pivot,
                                   Object settings, Object random, int flags) throws Throwable {
        long thread = Thread.currentThread().threadId();
        Long attempt = ACTIVE.get(thread);
        if (attempt == null || IN_TEMPLATE.putIfAbsent(thread, true) != null) {
            throw new IllegalStateException("Unpaired or nested BetterEnd template placement");
        }
        String path = TEMPLATE_PATHS.get(template);
        if (SHIP.replace('/', '.').equals(FEATURES.get(thread))) path = "minecraft:end_city/ship";
        if (path == null) throw new IllegalStateException("Placed template has no observed source path");
        emit("{\"kind\":\"template_begin\",\"attempt\":" + attempt + ",\"path\":"
            + quote(path) + ",\"position\":" + position(pos) + ",\"pivot\":" + position(pivot)
            + ",\"rotation\":" + quote(call(settings, "getRotation"))
            + ",\"mirror\":" + quote(call(settings, "getMirror")) + ",\"flags\":" + flags + "}");
        ClassLoader loader = world.getClass().getClassLoader();
        Method method = template.getClass().getMethod("placeInWorld",
            Class.forName("net.minecraft.world.level.ServerLevelAccessor", false, loader),
            Class.forName("net.minecraft.core.BlockPos", false, loader),
            Class.forName("net.minecraft.core.BlockPos", false, loader),
            Class.forName(TEMPLATE.replace("StructureTemplate", "StructurePlaceSettings").replace('/', '.'), false, loader),
            Class.forName("net.minecraft.util.RandomSource", false, loader), int.class);
        try {
            boolean returned = (Boolean) method.invoke(template, world, pos, pivot, settings, random, flags);
            emit("{\"kind\":\"template_end\",\"attempt\":" + attempt + ",\"returned\":" + returned + "}");
            return returned;
        } catch (InvocationTargetException error) {
            emit("{\"kind\":\"template_exception\",\"attempt\":" + attempt
                + ",\"exception\":" + quote(error.getCause().getClass().getName()) + "}");
            throw error.getCause();
        } finally {
            IN_TEMPLATE.remove(thread);
        }
    }

    public static boolean contentWrite(Object world, Object pos, Object state, int flags) throws Throwable {
        if (IN_TEMPLATE.containsKey(Thread.currentThread().threadId())) return write(world, pos, state, flags);
        // Outside a targeted placement, invoke the exact original interface method without tracing.
        ClassLoader loader = world.getClass().getClassLoader();
        Method method = Class.forName("net.minecraft.world.level.ServerLevelAccessor", false, loader)
            .getMethod("setBlock", Class.forName("net.minecraft.core.BlockPos", false, loader),
                Class.forName("net.minecraft.world.level.block.state.BlockState", false, loader), int.class);
        try {
            return (Boolean) method.invoke(world, pos, state, flags);
        } catch (InvocationTargetException error) {
            throw error.getCause();
        }
    }

    public static boolean directWrite(Object world, Object pos, Object state, int flags) throws Throwable {
        String feature = FEATURES.get(Thread.currentThread().threadId());
        if ("biomesoplenty.worldgen.feature.misc.AnomalyFeature".equals(feature)
            || "biomesoplenty.worldgen.feature.misc.MonolithFeature".equals(feature)) {
            return write(world, pos, state, flags);
        }
        ClassLoader loader = world.getClass().getClassLoader();
        Method method = Class.forName("net.minecraft.world.level.LevelWriter", false, loader)
            .getMethod("setBlock", Class.forName("net.minecraft.core.BlockPos", false, loader),
                Class.forName("net.minecraft.world.level.block.state.BlockState", false, loader), int.class);
        try {
            return (Boolean) method.invoke(world, pos, state, flags);
        } catch (InvocationTargetException error) {
            throw error.getCause();
        }
    }

    public static byte[] instrument(String target, byte[] original) {
        if (TARGET.equals(target)) return instrument(original);
        boolean direct = ANOMALY.equals(target) || MONOLITH.equals(target);
        boolean base = BASE_FEATURE.equals(target);
        boolean feature = END_FEATURE.equals(target) || SHIP.equals(target) || direct;
        boolean info = INFO.equals(target);
        if (!feature && !info && !base && !TEMPLATE.equals(target)) throw new IllegalArgumentException(target);
        ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_MAXS);
        int[] counts = new int[3];
        new ClassReader(original).accept(new ClassVisitor(Opcodes.ASM8, writer) {
            @Override
            public MethodVisitor visitMethod(int access, String name, String descriptor,
                                             String signature, String[] exceptions) {
                if (name.startsWith("item10$")) throw new IllegalArgumentException("Probe bridge collision");
                MethodVisitor parent = super.visitMethod(access, name, descriptor, signature, exceptions);
                boolean match = feature ? name.equals("place") && descriptor.equals(
                    "(Lnet/minecraft/world/level/levelgen/feature/FeaturePlaceContext;)Z")
                    : info ? name.equals("getStructure") && descriptor.equals("()L" + TEMPLATE + ";")
                    : base ? name.equals("setBlock") && descriptor.equals(BASE_WRITE)
                    : name.equals("placeInWorld") && descriptor.equals(TEMPLATE_DESCRIPTOR);
                if (!match) return parent;
                counts[0]++;
                return new MethodVisitor(Opcodes.ASM8, parent) {
                    @Override
                    public void visitCode() {
                        super.visitCode();
                        if (feature) {
                            super.visitVarInsn(Opcodes.ALOAD, 0);
                            super.visitVarInsn(Opcodes.ALOAD, 1);
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$beginFeature",
                                "(Ljava/lang/Object;Ljava/lang/Object;)V", false);
                        }
                    }
                    @Override
                    public void visitInsn(int opcode) {
                        if (feature && opcode == Opcodes.IRETURN) {
                            super.visitInsn(Opcodes.DUP);
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$end", "(Z)V", false);
                        } else if (info && opcode == Opcodes.ARETURN) {
                            counts[1]++;
                            super.visitInsn(Opcodes.DUP);
                            super.visitVarInsn(Opcodes.ALOAD, 0);
                            super.visitInsn(Opcodes.SWAP);
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$selected",
                                "(Ljava/lang/Object;Ljava/lang/Object;)V", false);
                        }
                        super.visitInsn(opcode);
                    }
                    @Override
                    public void visitMethodInsn(int opcode, String owner, String name,
                                                String descriptor, boolean isInterface) {
                        if (ANOMALY.equals(target) && opcode == Opcodes.INVOKEINTERFACE
                            && owner.equals("net/minecraft/world/level/WorldGenLevel")
                            && name.equals("setBlock") && descriptor.equals(WRITE_DESCRIPTOR)) {
                            counts[1]++;
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$write",
                                "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z", false);
                            return;
                        }
                        if (base && opcode == Opcodes.INVOKEINTERFACE
                            && owner.equals("net/minecraft/world/level/LevelWriter")
                            && name.equals("setBlock") && descriptor.equals(WRITE_DESCRIPTOR)) {
                            counts[1]++;
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$directWrite",
                                "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z", false);
                            return;
                        }
                        if (feature && opcode == Opcodes.INVOKEVIRTUAL && owner.equals(TEMPLATE)
                            && name.equals("placeInWorld") && descriptor.equals(TEMPLATE_DESCRIPTOR)) {
                            counts[1]++;
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$template", TEMPLATE_BRIDGE, false);
                            return;
                        }
                        if (!feature && !info && opcode == Opcodes.INVOKEINTERFACE
                            && owner.equals("net/minecraft/world/level/ServerLevelAccessor")
                            && name.equals("setBlock") && descriptor.equals(WRITE_DESCRIPTOR)) {
                            counts[1]++;
                            if (counts[1] == 2) {
                                super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$contentWrite",
                                    "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z", false);
                                return;
                            }
                        }
                        super.visitMethodInsn(opcode, owner, name, descriptor, isInterface);
                        if (END_FEATURE.equals(target) && opcode == Opcodes.INVOKEVIRTUAL
                            && owner.equals(END_FEATURE) && name.equals("getGround")
                            && descriptor.equals("(Lnet/minecraft/world/level/WorldGenLevel;Lnet/minecraft/core/BlockPos;)Lnet/minecraft/core/BlockPos;")) {
                            counts[2]++;
                            super.visitInsn(Opcodes.DUP);
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, target, "item10$ground",
                                "(Ljava/lang/Object;)V", false);
                        }
                    }
                };
            }
        }, 0);
        if (counts[0] != 1 || counts[1] != (direct ? (ANOMALY.equals(target) ? 1 : 0) : feature || info || base ? 1 : 3)) {
            throw new IllegalArgumentException("Unexpected template hook sites: " + target
                + " " + counts[0] + "," + counts[1]);
        }
        if (END_FEATURE.equals(target)) {
            if (counts[2] != 1) throw new IllegalArgumentException("Unexpected ground hook count");
            bridge(writer, "ground", "(Ljava/lang/Object;)V", new int[] {Opcodes.ALOAD}, Opcodes.RETURN);
        }
        if (feature) {
            bridge(writer, "beginFeature", "(Ljava/lang/Object;Ljava/lang/Object;)V",
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD}, Opcodes.RETURN);
            bridge(writer, "end", "(Z)V", new int[] {Opcodes.ILOAD}, Opcodes.RETURN);
            if (ANOMALY.equals(target)) bridge(writer, "write",
                "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z",
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ILOAD}, Opcodes.IRETURN);
            if (!direct) bridge(writer, "template", TEMPLATE_BRIDGE,
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ILOAD}, Opcodes.IRETURN);
        } else if (base) {
            bridge(writer, "directWrite", "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z",
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ILOAD}, Opcodes.IRETURN);
        } else if (info) {
            bridge(writer, "selected", "(Ljava/lang/Object;Ljava/lang/Object;)V",
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD}, Opcodes.RETURN);
        } else {
            bridge(writer, "contentWrite", "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z",
                new int[] {Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ILOAD}, Opcodes.IRETURN);
        }
        return writer.toByteArray();
    }

    public static byte[] instrument(byte[] original) {
        ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_MAXS);
        int[] counts = new int[2];
        new ClassReader(original).accept(new ClassVisitor(Opcodes.ASM8, writer) {
            @Override
            public MethodVisitor visitMethod(int access, String name, String descriptor,
                                             String signature, String[] exceptions) {
                if (name.startsWith("item10$")) {
                    throw new IllegalArgumentException("Probe bridge name collision: " + name);
                }
                MethodVisitor parent = super.visitMethod(access, name, descriptor, signature, exceptions);
                if (!name.equals("place") || !descriptor.equals(
                    "(Lnet/minecraft/world/level/levelgen/feature/FeaturePlaceContext;)Z")) {
                    return parent;
                }
                counts[0]++;
                return new MethodVisitor(Opcodes.ASM8, parent) {
                    @Override
                    public void visitCode() {
                        super.visitCode();
                        super.visitVarInsn(Opcodes.ALOAD, 1);
                        super.visitMethodInsn(Opcodes.INVOKESTATIC, TARGET, "item10$begin",
                            "(Ljava/lang/Object;)V", false);
                    }
                    @Override
                    public void visitInsn(int opcode) {
                        if (opcode == Opcodes.IRETURN) {
                            super.visitInsn(Opcodes.DUP);
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, TARGET, "item10$end",
                                "(Z)V", false);
                        }
                        super.visitInsn(opcode);
                    }
                    @Override
                    public void visitMethodInsn(int opcode, String owner, String name,
                                                String descriptor, boolean isInterface) {
                        if (opcode == Opcodes.INVOKEINTERFACE
                            && owner.equals("net/minecraft/world/level/WorldGenLevel")
                            && name.equals("setBlock") && descriptor.equals(WRITE_DESCRIPTOR)) {
                            counts[1]++;
                            super.visitMethodInsn(Opcodes.INVOKESTATIC, TARGET, "item10$write",
                                "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z", false);
                        } else {
                            super.visitMethodInsn(opcode, owner, name, descriptor, isInterface);
                        }
                    }
                };
            }
        }, 0);
        if (counts[0] != 1 || counts[1] != 5) {
            throw new IllegalArgumentException("Expected one place method and five writes, got "
                + counts[0] + "," + counts[1]);
        }
        bridge(writer, "begin", "(Ljava/lang/Object;)V", new int[] {Opcodes.ALOAD}, Opcodes.RETURN);
        bridge(writer, "end", "(Z)V", new int[] {Opcodes.ILOAD}, Opcodes.RETURN);
        bridge(writer, "write", "(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;I)Z",
            new int[] {Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ALOAD, Opcodes.ILOAD}, Opcodes.IRETURN);
        return writer.toByteArray();
    }

    // Game module loaders cannot resolve the application-loader helper directly.
    // Resolve explicitly through java.base; invokeExact preserves original thrown exceptions.
    private static void bridge(ClassWriter writer, String name, String descriptor,
                               int[] loads, int returnOpcode) {
        MethodVisitor method = writer.visitMethod(
            Opcodes.ACC_PRIVATE | Opcodes.ACC_STATIC | Opcodes.ACC_SYNTHETIC,
            "item10$" + name, descriptor, null, null);
        method.visitCode();
        method.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/invoke/MethodHandles", "publicLookup",
            "()Ljava/lang/invoke/MethodHandles$Lookup;", false);
        method.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/ClassLoader", "getSystemClassLoader",
            "()Ljava/lang/ClassLoader;", false);
        method.visitLdcInsn("Item10PlacementProbe");
        method.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/ClassLoader", "loadClass",
            "(Ljava/lang/String;)Ljava/lang/Class;", false);
        method.visitLdcInsn(name);
        method.visitLdcInsn(descriptor);
        method.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/ClassLoader", "getSystemClassLoader",
            "()Ljava/lang/ClassLoader;", false);
        method.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/invoke/MethodType", "fromMethodDescriptorString",
            "(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljava/lang/invoke/MethodType;", false);
        method.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/invoke/MethodHandles$Lookup", "findStatic",
            "(Ljava/lang/Class;Ljava/lang/String;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/MethodHandle;", false);
        for (int index = 0; index < loads.length; index++) method.visitVarInsn(loads[index], index);
        method.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/invoke/MethodHandle", "invokeExact", descriptor, false);
        method.visitInsn(returnOpcode);
        method.visitMaxs(0, 0);
        method.visitEnd();
    }

    public static void premain(String destination, Instrumentation instrumentation) throws Exception {
        output = Path.of(destination);
        Files.writeString(output, "", StandardOpenOption.CREATE_NEW);
        Runtime.getRuntime().addShutdownHook(new Thread(() -> emit(
            "{\"kind\":\"shutdown\",\"installed\":" + installed
            + ",\"unfinished_attempts\":" + ACTIVE.size() + "}")));
        instrumentation.addTransformer(new ClassFileTransformer() {
            @Override
            public byte[] transform(Module module, ClassLoader loader, String name,
                                    Class<?> previous, ProtectionDomain domain, byte[] bytes) {
                if (!TARGET.equals(name) && !END_FEATURE.equals(name) && !SHIP.equals(name)
                    && !INFO.equals(name) && !TEMPLATE.equals(name)
                    && !ANOMALY.equals(name) && !MONOLITH.equals(name) && !BASE_FEATURE.equals(name)) {
                    return null;
                }
                try {
                    Path incoming = output.toAbsolutePath().getParent().resolve(output.getFileName() + ".classes")
                        .resolve(name + ".class");
                    Files.createDirectories(incoming.getParent());
                    Files.write(incoming, bytes, StandardOpenOption.CREATE_NEW);
                    byte[] result = instrument(name, bytes);
                    String sha = HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256").digest(bytes));
                    if (TARGET.equals(name)) {
                        emit("{\"kind\":\"installed\",\"input_class_sha256\":" + quote(sha) + "}");
                        installed = true;
                    } else {
                        emit("{\"kind\":\"feature_installed\",\"class\":" + quote(name)
                            + ",\"input_class_sha256\":" + quote(sha) + "}");
                    }
                    return result;
                } catch (Throwable error) {
                    emit("{\"kind\":\"installation_failed\",\"exception\":" + quote(error.toString()) + "}");
                    throw new IllegalStateException("Placement instrumentation failed", error);
                }
            }
        });
    }
}
