package finding;

import java.util.HashMap;

public class FindValue {
    public static <K,V> V findValueByKey(HashMap<K,V> map, K klucz)
    {
        try
        {
            if (klucz == null)
            {
                throw new IllegalArgumentException("Key cannot be null");
            }
            return map.get(klucz);
        }
        catch (NullPointerException e)
        {
            // Obsługa ewentualnego wyjątku związanego z przekazaniem null jako argumentu
            System.err.println("Error: " + e.getMessage());
            return null;
        }
    }

    public static void main(String[] args) {
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("one", 1);
        hashMap.put("two", 2);
        hashMap.put("three", 3);

        String keyToFind = "two";
        Integer result = findValueByKey(hashMap, keyToFind);
        System.out.println("Value for key '" + keyToFind + "': " + result);
    }

}

