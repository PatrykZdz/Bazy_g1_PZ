package algorithm;

import java.util.HashMap;

public class Algorithm {

    public static <K, V> boolean areValuesEqual(HashMap<K, V> map, K key1, K key2) {
        if (map == null || key1 == null || key2 == null) {
            throw new IllegalArgumentException();
        }

        V value1 = map.get(key1);
        V value2 = map.get(key2);

        if (value1 == null && value2 == null) {
            return true; // Jeśli obie wartości są null, uważamy je za równe
        }

        return value1 != null && value1.equals(value2);
    }
}
