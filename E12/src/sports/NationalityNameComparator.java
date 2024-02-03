package sports;

import java.util.Comparator;
import java.util.Objects;

public class NationalityNameComparator implements Comparator<Athlete> {
    @Override
    public int compare(Athlete o1, Athlete o2) {
        int nationalityComparison = o2.getNationality().compareTo(o1.getNationality());

        if (nationalityComparison == 0) {
            // Porównaj imię i nazwisko w normalnej kolejności
            return o1.getName().compareTo(o2.getName());
        } else {
            return nationalityComparison;
        }
    }
}
