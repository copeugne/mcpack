import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import org.apache.maven.artifact.versioning.DefaultArtifactVersion;
import org.apache.maven.artifact.versioning.InvalidVersionSpecificationException;
import org.apache.maven.artifact.versioning.VersionRange;

public final class MavenVersionRangeProbe {
    private MavenVersionRangeProbe() {}

    public static void main(String[] arguments) throws IOException {
        if (arguments.length != 0) {
            System.err.println("usage: provide case_id, version, and range as TSV on standard input");
            System.exit(64);
        }
        try (var reader = new BufferedReader(
                new InputStreamReader(System.in, StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                var fields = line.split("\\t", -1);
                if (fields.length != 3) {
                    System.out.printf("%s\tinvalid\texpected_3_fields%n", fields[0]);
                    continue;
                }
                emit(fields[0], fields[1], fields[2]);
            }
        }
    }

    private static void emit(String caseId, String version, String specification) {
        try {
            var range = VersionRange.createFromVersionSpec(specification);
            var candidate = new DefaultArtifactVersion(version);
            var status = range.containsVersion(candidate) ? "pass" : "fail";
            System.out.printf("%s\t%s\t%s%n", caseId, status, range);
        } catch (InvalidVersionSpecificationException exception) {
            var detail = exception.getMessage().replace('\t', ' ').replace('\n', ' ');
            System.out.printf("%s\tinvalid\t%s%n", caseId, detail);
        }
    }
}
