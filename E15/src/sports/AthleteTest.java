package sports;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class AthleteTest {
    public static void main(String[] args) {

        List<Athlete> athletes = new ArrayList<>();
        athletes.add(new Athlete("Marek","Bieg",1999));
        athletes.add(new Athlete("Kuba","Plywanie",2030));
        athletes.add(new Athlete("Maciek","Rzut kula",2014));
        athletes.add(new Athlete("Jakub","Bieg przez plodki",1960));

        Collections.sort(athletes);
        for(int i = 0; i < athletes.size();i++)
        {
            System.out.println(athletes.get(i));
        }
    }
}
