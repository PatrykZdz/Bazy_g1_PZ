package algorithm;

import java.util.HashMap;

public class TestAlgorithm {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "value1");
        map.put(2, "value2");
        map.put(3, "value3");

        System.out.println(Algorithm.areValuesEqual(map, 1, 2)); // Powinno zwrócić false
        System.out.println(Algorithm.areValuesEqual(map, 1, 3)); // Powinno zwrócić false
        System.out.println(Algorithm.areValuesEqual(map, 2, 3)); // Powinno zwrócić false
        System.out.println(Algorithm.areValuesEqual(map, 1, 1)); // Powinno zwrócić true
        System.out.println(Algorithm.areValuesEqual(map, 2, 2)); // Powinno zwrócić true
        System.out.println(Algorithm.areValuesEqual(map, 3, 3)); // Powinno zwrócić true
        System.out.println(Algorithm.areValuesEqual(map, 1, 4)); // Powinno zwrócić false, gdyż klucz 4 nie istnieje w mapie
    }
}
