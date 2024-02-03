package algorithm;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Mapa {

    public static <K,V> String mapToString(HashMap<K,V> map)
    {
        List<Map.Entry<K,V>> entryList = new ArrayList<>(map.entrySet());
        String result = "";

        for(int i = 0; i< entryList.size();i++)
        {
            K key = entryList.get(i).getKey();
            V value = entryList.get(i).getValue();

             result = result+key+": "+value+", ";
        }
        return result;
    }


    /*public static <K, V> String mapToString(HashMap<K, V> map) {
        List<Map.Entry<K, V>> entryList = new ArrayList<>(map.entrySet());
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < entryList.size(); i++) {
            K key = entryList.get(i).getKey();
            V value = entryList.get(i).getValue();

            result.append(key)
                    .append(": ")
                    .append(value)
                    .append(", ");
        }

        // Usunięcie ostatniej przecinki i spacji, jeśli mapa nie jest pusta
        if (!map.isEmpty()) {
            result.delete(result.length() - 2, result.length());
        }

        return result.toString();
    }*/

}
