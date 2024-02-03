package utilities;


public class Count {

    public static <T extends Comparable<T>> int countLessThanOrEqual(T[] tablica,T arg)
    {
        for(int i = 0; i < tablica.length;i++)
        {
            if(tablica[i].compareTo(arg) < 0)
            {
                return i+1;
            }
        }
        return tablica.length;
    }

}
