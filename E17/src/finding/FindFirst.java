package finding;

public class FindFirst {

    public static <T> T findFirstNonNUll(T[] tablica)
    {
        for(int i = 0; i < tablica.length;i++)
        {
            if(tablica[i] != null) {
                return tablica[i];
            }
        }
       return null;
    }
}
