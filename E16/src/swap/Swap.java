package swap;

import javax.xml.stream.events.StartElement;
import java.util.Arrays;

public class Swap {
    public static <T> void swapElements(T[] tablica, int indeks1, int indeks2)
    {
        T temp = tablica[indeks1];
        tablica[indeks1] = tablica[indeks2];
        tablica[indeks2] = temp;

    }
}
