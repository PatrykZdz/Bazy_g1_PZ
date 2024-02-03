package algorithm;

import java.util.HashMap;
import java.util.Map;

public class Count {

    public static <K, V> int countUniqueKeys(HashMap<K,V> arg)
    {
        return arg.keySet().size();
    }

}
