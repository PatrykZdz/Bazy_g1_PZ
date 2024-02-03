package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Mapa {

    public static <K, V> String mapToString(HashMap<K, V> map)
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


}

