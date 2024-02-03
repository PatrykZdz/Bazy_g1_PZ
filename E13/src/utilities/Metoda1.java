package utilities;

public class Metoda1 {
/// nie implements tylko extends
    public static <T extends Comparable<T>> T findMin(T wartosc1, T wartosc2, T wartosc3)
    {
        T min = wartosc1;
        if(wartosc2.compareTo(min) < 0) // < 0 Mniejsza wartosc, > 0 Wieksza wartosc
        {
            min = wartosc2;
        }
        if(wartosc3.compareTo(min)< 0)
        {
            min = wartosc3;
        }
        return min;

    }

    public static void main(String[] args) {
        Integer wartosc = findMin(1,2,3);
        System.out.println(wartosc);
    }

}
