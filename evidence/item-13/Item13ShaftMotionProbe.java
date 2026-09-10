import java.lang.instrument.Instrumentation;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.HexFormat;
import java.security.MessageDigest;
import java.util.zip.GZIPInputStream;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;

/** One native FakePlayer motion pilot, not a connected player or gameplay trial. */
public final class Item13ShaftMotionProbe {
    private static ClassLoader loader;
    private static Class<?> type(String name) throws ClassNotFoundException {
        return Class.forName(name, true, loader);
    }
    private static Object call(Object object, String name, Class<?>[] signature, Object... args)
            throws Exception {
        return object.getClass().getMethod(name, signature).invoke(object, args);
    }
    private static Object get(Object object, String name) throws Exception {
        return call(object, name, new Class<?>[0]);
    }
    private static double number(Object object, String name) throws Exception {
        return ((Number)get(object, name)).doubleValue();
    }
    private static List<Double> position(Object actor) throws Exception {
        return List.of(number(actor,"getX"),number(actor,"getY"),number(actor,"getZ"));
    }
    public static void agentmain(String output, Instrumentation instrumentation) throws Exception {
        Object server = null;
        for (Class<?> candidate : instrumentation.getAllLoadedClasses()) {
            if (candidate.getName().equals("net.neoforged.neoforge.server.ServerLifecycleHooks")) {
                if (server != null) throw new IllegalStateException("Duplicate lifecycle class");
                server = candidate.getMethod("getCurrentServer").invoke(null);
            }
        }
        if (server == null) throw new IllegalStateException("No active server");
        loader = server.getClass().getClassLoader();
        Object level = call(server,"getLevel",new Class<?>[]{type("net.minecraft.resources.ResourceKey")},
            type("net.minecraft.world.level.Level").getField("OVERWORLD").get(null));
        if (level == null) throw new IllegalStateException("Overworld missing");
        Object source = get(level,"getChunkSource");
        Class<?> status = type("net.minecraft.world.level.chunk.status.ChunkStatus");
        // Load only the preflight-verified full saved chunk; never select a new region.
        List<CompletableFuture<?>> pending = new ArrayList<>();
        for (int cx=12;cx<=12;cx++) for (int cz=21;cz<=21;cz++) {
            pending.add((CompletableFuture<?>)call(source,"getChunkFuture",
                new Class<?>[]{int.class,int.class,status,boolean.class},cx,cz,
                status.getField("FULL").get(null),true));
        }
        CompletableFuture.allOf(pending.toArray(new CompletableFuture<?>[0])).get(30,TimeUnit.SECONDS);
        String mode=Path.of(output).getFileName().toString();
        if (!mode.equals("shaft-motion.json") && !mode.equals("shaft-motion-full.json"))
            throw new IllegalArgumentException("Unknown shaft case");
        boolean full=mode.equals("shaft-motion-full.json");
        FutureTask<Map<String,Object>> trial = new FutureTask<>(() -> motion(level,Path.of(output).resolveSibling("input.json.gz"),full));
        call(server,"execute",new Class<?>[]{Runnable.class},trial);
        Map<String,Object> result = trial.get(30,TimeUnit.SECONDS);
        Object gson = type("com.google.gson.Gson").getConstructor().newInstance();
        Files.writeString(Path.of(output),(String)call(gson,"toJson",new Class<?>[]{Object.class},result)+"\n",
            StandardCharsets.UTF_8,StandardOpenOption.CREATE_NEW);
        if (result.get("rejection_reason") != null)
            throw new IllegalStateException("Motion pilot rejected; retained result describes failure");
    }
    private static Map<String,Object> motion(Object level, Path input, boolean full) throws Exception {
        Map<String,Object> result = new LinkedHashMap<>();
        List<Map<String,Object>> rows = new ArrayList<>();
        result.put("method","Native manually stepped FakePlayer baseTick/aiStep; stationary world during query");
        result.put("steps",rows);
        result.put("case",full?"continuous-shaft-return":"one-rising-step");
        List<List<Double>> targets=new ArrayList<>();
        if (full) {
            int[][] perimeter={{195,342},{195,341},{196,341},{197,341},{197,342},{197,343},{196,343},{195,343}};
            for (int i=0;i<17;i++) targets.add(List.of(perimeter[i%8][0]+.5,8.5+i,perimeter[i%8][1]+.5));
            targets.add(List.of(196.5,25.5,342.5));
            targets.add(List.of(194.5,26.,342.5));
            targets.add(List.of(196.5,25.5,342.5));
            for (int i=16;i>=0;i--) targets.add(List.of(perimeter[i%8][0]+.5,8.5+i,perimeter[i%8][1]+.5));
            targets.add(List.of(195.5,8.,343.5));
        } else targets.add(List.of(195.5,9.5,341.5));
        result.put("targets",targets);
        List<Map<String,Object>> landings=new ArrayList<>();
        result.put("landings",landings);
        result.put("rejection_reason","pilot incomplete");
        Object actor = null;
        try {
            String hash = HexFormat.of().formatHex(MessageDigest.getInstance("SHA-256").digest(Files.readAllBytes(input)));
            result.put("input_sha256",hash);
            if (!hash.equals("faed7df352cdcfc1938fb4d49f4f84b2519ad4f1ee55044fa661ae55e6f81d5c"))
                throw new IllegalStateException("Saved geometry input hash mismatch");
            Object gson = type("com.google.gson.Gson").getConstructor().newInstance();
            String text;
            try (var stream = new GZIPInputStream(Files.newInputStream(input))) {
                text = new String(stream.readAllBytes(),StandardCharsets.UTF_8);
            }
            Map<?,?> document = (Map<?,?>)call(gson,"fromJson",new Class<?>[]{String.class,Class.class},text,Map.class);
            Map<?,?> saved = (Map<?,?>)((List<?>)document.get("cases")).get(0);
            List<?> bounds = (List<?>)saved.get("bounds"), blocks = (List<?>)saved.get("blocks_yzx"), palette = (List<?>)saved.get("palette");
            int minX=((Number)bounds.get(0)).intValue(), minY=((Number)bounds.get(1)).intValue(), minZ=((Number)bounds.get(2)).intValue();
            int width=((Number)bounds.get(3)).intValue()-minX+1, depth=((Number)bounds.get(5)).intValue()-minZ+1;
            Object registry = type("net.minecraft.core.registries.BuiltInRegistries").getField("BLOCK").get(null);
            Class<?> propertyType = type("net.minecraft.world.level.block.state.properties.Property");
            // UUID is ephemeral, never emitted, registered with a player list or persisted.
            Object profile = type("com.mojang.authlib.GameProfile").getConstructor(UUID.class,String.class)
                .newInstance(UUID.randomUUID(),"Item13Motion");
            actor = type("net.neoforged.neoforge.common.util.FakePlayer")
                .getConstructor(type("net.minecraft.server.level.ServerLevel"),type("com.mojang.authlib.GameProfile"))
                .newInstance(level,profile);
            call(actor,"setPos",new Class<?>[]{double.class,double.class,double.class},195.5,full?8.:8.5,full?343.5:342.5);
            call(actor,"setDeltaMovement",new Class<?>[]{double.class,double.class,double.class},0.0,0.0,0.0);
            call(actor,"setOnGround",new Class<?>[]{boolean.class},true);
            if (Math.abs(number(actor,"getBbWidth")-.6)>1e-6 || Math.abs(number(actor,"getBbHeight")-1.8)>1e-6)
                throw new IllegalStateException("Actor dimensions differ from declared adult");
            result.put("actor_dimensions",List.of(number(actor,"getBbWidth"),number(actor,"getBbHeight")));
            if (!((java.util.Collection<?>)get(actor,"getActiveEffects")).isEmpty())
                throw new IllegalStateException("Unexpected actor effects");
            Map<String,Double> attributes = new LinkedHashMap<>();
            String[] names={"MOVEMENT_SPEED","JUMP_STRENGTH","GRAVITY","WATER_MOVEMENT_EFFICIENCY","STEP_HEIGHT"};
            double[] expectedAttributes={.1,.41999998688697815,.08,0,.6};
            for (int i=0;i<names.length;i++) {
                Object holder=type("net.minecraft.world.entity.ai.attributes.Attributes").getField(names[i]).get(null);
                double value=((Number)call(actor,"getAttributeValue",new Class<?>[]{type("net.minecraft.core.Holder")},holder)).doubleValue();
                attributes.put(names[i],value);
                if (Math.abs(value-expectedAttributes[i])>1e-6)
                    throw new IllegalStateException("Actor attribute differs: "+names[i]);
            }
            result.put("attributes",attributes);
            call(actor,"setSprinting",new Class<?>[]{boolean.class},false);
            Object abilities = get(actor,"getAbilities");
            if (abilities.getClass().getField("flying").getBoolean(abilities)
                    || abilities.getClass().getField("mayfly").getBoolean(abilities))
                throw new IllegalStateException("Flight capability enabled");
            Class<?> blockPos = type("net.minecraft.core.BlockPos");
            List<String> initial = new ArrayList<>();
            result.put("initial_states_xyz",initial);
            for (int x=full?193:194;x<=(full?200:198);x++) for (int y=full?6:7;y<=(full?31:13);y++) for (int z=full?339:340;z<=(full?346:344);z++) {
                Object p = blockPos.getConstructor(int.class,int.class,int.class).newInstance(x,y,z);
                Object state = call(level,"getBlockState",new Class<?>[]{blockPos},p);
                Map<String,Object> actual = new LinkedHashMap<>();
                actual.put("Name",call(registry,"getKey",new Class<?>[]{Object.class},get(state,"getBlock")).toString());
                Map<String,String> properties = new LinkedHashMap<>();
                for (var entry : ((Map<?,?>)get(state,"getValues")).entrySet()) {
                    properties.put((String)propertyType.getMethod("getName").invoke(entry.getKey()),
                        (String)propertyType.getMethod("getName",Comparable.class).invoke(entry.getKey(),entry.getValue()));
                }
                if (!properties.isEmpty()) actual.put("Properties",properties);
                int index=((y-minY)*depth+z-minZ)*width+x-minX;
                Object expected=palette.get(((Number)blocks.get(index)).intValue());
                initial.add(state.toString());
                if (!actual.equals(expected)) throw new IllegalStateException("Loaded geometry differs at "+x+","+y+","+z);
            }
            Class<?> boxType=type("net.minecraft.world.phys.AABB");
            Object box=boxType.getConstructor(double.class,double.class,double.class,double.class,double.class,double.class)
                .newInstance(193.,full?6.:7.,339.,200.,full?31.:14.,346.);
            List<?> entities=(List<?>)call(level,"getEntities",new Class<?>[]{type("net.minecraft.world.entity.Entity"),boxType},null,box);
            result.put("nearby_entities",entities.size());
            if (!entities.isEmpty()) throw new IllegalStateException("Other entities occupy pilot scope");
            int targetIndex=0, targetStart=0;
            for (int tick=0;tick<=120*targets.size();tick++) {
                List<Double> target=targets.get(targetIndex);
                Map<String,Object> row = new LinkedHashMap<>();
                row.put("step",tick); row.put("target_index",targetIndex); row.put("position",position(actor));
                row.put("on_ground",get(actor,"onGround")); row.put("in_water",get(actor,"isInWater"));
                row.put("pose",get(actor,"getPose").toString()); row.put("height",number(actor,"getBbHeight"));
                Object velocity = get(actor,"getDeltaMovement");
                row.put("velocity",List.of(velocity.getClass().getField("x").getDouble(velocity),
                    velocity.getClass().getField("y").getDouble(velocity),velocity.getClass().getField("z").getDouble(velocity)));
                rows.add(row);
                double dx=target.get(0)-number(actor,"getX"),dz=target.get(2)-number(actor,"getZ");
                if (tick>targetStart && Math.hypot(dx,dz)<=.15 && Math.abs(number(actor,"getY")-target.get(1))<1e-5
                        && Boolean.TRUE.equals(get(actor,"onGround"))) {
                    landings.add(Map.of("target_index",targetIndex,"step",tick,"position",position(actor)));
                    targetIndex++;
                    if (targetIndex==targets.size()) { result.put("rejection_reason",null); break; }
                    targetStart=tick;
                    target=targets.get(targetIndex);
                    dx=target.get(0)-number(actor,"getX"); dz=target.get(2)-number(actor,"getZ");
                }
                if (tick-targetStart>=120) throw new IllegalStateException("No landing at target "+targetIndex+" within 120 native steps");
                if (number(actor,"getY")<7.5 || (full && number(actor,"getY")>27.5) || Math.hypot(dx,dz)>3)
                    throw new IllegalStateException("Actor left the predeclared local scope at target "+targetIndex);
                if (full) {
                    boolean crouch=targetIndex>=17 && targetIndex<=20;
                    call(actor,"setShiftKeyDown",new Class<?>[]{boolean.class},crouch);
                    Class<?> pose=type("net.minecraft.world.entity.Pose");
                    call(actor,"setPose",new Class<?>[]{pose},pose.getField(crouch?"CROUCHING":"STANDING").get(null));
                    if (Math.abs(number(actor,"getBbHeight")-(crouch?1.5:1.8))>1e-6)
                        throw new IllegalStateException("Unexpected pose height");
                    if (!Boolean.TRUE.equals(call(level,"noCollision",new Class<?>[]{type("net.minecraft.world.entity.Entity")},actor)))
                        throw new IllegalStateException("Pose collides at target "+targetIndex);
                }
                call(actor,"baseTick",new Class<?>[0]);
                call(actor,"setYRot",new Class<?>[]{float.class},(float)Math.toDegrees(Math.atan2(-dx,dz)));
                call(actor,"setXRot",new Class<?>[]{float.class},0f);
                type("net.minecraft.world.entity.LivingEntity").getField("xxa").setFloat(actor,0f);
                type("net.minecraft.world.entity.LivingEntity").getField("zza").setFloat(actor,Math.hypot(dx,dz)>.05?(full && targetIndex>=17 && targetIndex<=20?.3f:1f):0f);
                call(actor,"setJumping",new Class<?>[]{boolean.class},number(actor,"getY")<target.get(1)-.1 || (full && targetIndex==19));
                call(actor,"aiStep",new Class<?>[0]);
            }
        } catch (Exception failure) {
            result.put("rejection_reason",failure.toString());
        } finally {
            if (actor != null) {
                try { call(actor,"discard",new Class<?>[0]); }
                catch (Exception failure) { result.put("rejection_reason","Actor cleanup failed: "+failure); }
            }
        }
        return result;
    }
}
