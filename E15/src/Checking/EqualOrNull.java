package Checking;

public class EqualOrNull {
    public static <T> boolean isEqualOrNull(T item1, T item2)
    {

        if(item1 == null && item2 == null)
            return true;
        if(item1 == null || item2 == null)
            return false;
        return item1.equals(item2);

    }
}
