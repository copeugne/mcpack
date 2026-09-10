import java.util.HashSet;
import java.util.Random;
import java.util.Set;

/** Source-derived coordinate selection, not an observed generation result. */
public final class SelectOrigins {
    private static String outcome(int x, int y, int z, boolean basalt) {
        // Pinned Mth.getSeed(int,int,int): preserve int overflow before long XOR.
        long seed = (long) (x * 3129871) ^ (long) z * 116129781L ^ (long) y;
        seed = (seed * seed * 42317861L + seed * 11L) >> 16;
        Random random = new Random(seed);
        if (random.nextFloat() < 0.2F) return basalt ? "netherite_block" : "ancient_debris";
        if (random.nextFloat() < 0.1F) return "lodestone";
        return basalt ? "ancient_debris" : "gold_block";
    }

    public static void main(String[] args) {
        if (args.length == 1 && args[0].equals("--basalt")) {
            int[][] centers = {{-3,15,-499},{157,15,-141},{-77,15,499},{499,15,467},
                {131,15,-189},{189,15,115},{-61,15,173},{141,15,355}};
            for (int i = 0; i < centers.length; i++) {
                int[] c = centers[i];
                String expected = i == 3 ? "lodestone" : "ancient_debris";
                if (!outcome(c[0],c[1],c[2],true).equals(expected))
                    throw new IllegalStateException("Basalt predictor disagrees with retained center " + i);
            }
            for (int i = 0; i < 256; i++) {
                int x = 32*(i%16), z = 32*(i/16);
                if (outcome(x+3,163,z+3,true).equals("netherite_block")) {
                    System.out.println("{\"evidence_class\":\"SOURCE-DERIVED SELECTION, NOT OBSERVED OUTCOME\",\"selected\":["
                        + "{\"template\":\"adorabuild_structures:basalt_chambers/ancient_debris\","
                        + "\"origin\":["+x+",160,"+z+"],\"expected_central_material\":\"minecraft:netherite_block\","
                        + "\"grid_index\":"+i+"}]}");
                    return;
                }
            }
            throw new IllegalStateException("No netherite origin in the declared grid");
        }
        if (args.length != 0) throw new IllegalArgumentException("Only --basalt or no arguments accepted");
        if (!outcome(467,35,-125,false).equals("gold_block")
                || !outcome(314,35,490,false).equals("gold_block"))
            throw new IllegalStateException("Source predictor disagrees with existing gold cases");
        Set<Integer> occupied = new HashSet<>();
        String[] roots = {"blackstone_temple_small_1", "nether_temple_medium_1"};
        int[] centers = {3,6};
        System.out.println("{\"evidence_class\":\"SOURCE-DERIVED SELECTION, NOT OBSERVED OUTCOMES\",\"selected\":[");
        boolean comma = false;
        for (int root = 0; root < roots.length; root++) {
            for (String material : new String[]{"ancient_debris", "lodestone"}) {
                int chosen = -1;
                for (int i = 0; i < 256; i++) {
                    if (!occupied.contains(i)
                            && outcome(32*(i%16)+centers[root],164,32*(i/16)+centers[root],false).equals(material)) {
                        chosen = i;
                        break;
                    }
                }
                if (chosen < 0) throw new IllegalStateException("No candidate in declared 256-origin grid");
                occupied.add(chosen);
                if (comma) System.out.println(",");
                System.out.print("{\"template\":\"adorabuild_structures:"+roots[root]
                    +"\",\"origin\":["+32*(chosen%16)+",160,"+32*(chosen/16)
                    +"],\"expected_central_material\":\"minecraft:"+material+"\",\"grid_index\":"+chosen+"}");
                comma = true;
            }
        }
        System.out.println("\n]}");
    }
}
