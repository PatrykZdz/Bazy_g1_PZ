package sports;

import java.util.Arrays;

public class TestAthlete {
    public static void main(String[] args)
    {
        Athlete[] athletes = {new Athlete("Bolt", "Jamaica", new double[]{9.58, 19.19}),
                new Athlete("Gatlin", "USA", new double[]{9.74, 19.57}),
                new Athlete("Blake", "Jamaica", new double[]{9.69, 19.26}),
                new Athlete("Bolt", "-", new double[]{9.58, 19.19})};

        Arrays.sort(athletes, new RecordComparator().thenComparing(new NationalityNameComparator()));
        for(int i = 0; i < athletes.length;i++)
        {
            System.out.println(athletes[i]);
        }
    }
}
