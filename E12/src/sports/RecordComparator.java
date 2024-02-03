package sports;

import java.util.Arrays;
import java.util.Comparator;

public class RecordComparator implements Comparator<Athlete> {
    @Override
    public int compare(Athlete o1, Athlete o2) {
        return Arrays.compare(o1.getRecords(),o2.getRecords());
    }
}
