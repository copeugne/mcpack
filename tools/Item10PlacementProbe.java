import java.lang.instrument.ClassFileTransformer;
import java.lang.instrument.Instrumentation;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.security.ProtectionDomain;
import java.util.HexFormat;
import java.security.MessageDigest;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import jdk.internal.org.objectweb.asm.ClassReader;
import jdk.internal.org.objectweb.asm.ClassVisitor;
import jdk.internal.org.objectweb.asm.ClassWriter;
import jdk.internal.org.objectweb.asm.MethodVisitor;
import jdk.internal.org.objectweb.asm.Opcodes;

/** Diagnostic only: trace the five direct scarecrow writes, preserving original results. */
public final class Item10PlacementProbe {
    private static final String TARGET =
        "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature";
    private static final String WRITE_DESCRIPTOR =
        "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;I)Z";
    private static final AtomicLong SEQUENCE = new AtomicLong();
    private static final ConcurrentHashMap<Long, Long> ACTIVE = new ConcurrentHashMap<>();
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
        Long id = ACTIVE.remove(Thread.currentThread().threadId());
        if (id == null) {
            throw new IllegalStateException("Exit outside traced attempt");
        }
        emit("{\"kind\":\"end\",\"attempt\":" + id + ",\"returned\":" + returned + "}");
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
                if (!TARGET.equals(name)) {
                    return null;
                }
                try {
                    byte[] result = instrument(bytes);
                    String sha = HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256").digest(bytes));
                    emit("{\"kind\":\"installed\",\"input_class_sha256\":" + quote(sha) + "}");
                    installed = true;
                    return result;
                } catch (Throwable error) {
                    emit("{\"kind\":\"installation_failed\",\"exception\":" + quote(error.toString()) + "}");
                    throw new IllegalStateException("Scarecrow instrumentation failed", error);
                }
            }
        });
    }
}
