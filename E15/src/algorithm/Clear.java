package algorithm;

import java.util.Collection;

public class Clear {
    public static <T> void clearIfContains(Collection<T> collections, T element)
    {
        if(collections == null)
            throw new IllegalArgumentException("Kolekcja nie moze byc null");
        if(collections.contains(element))
            collections.clear();



    }
}
