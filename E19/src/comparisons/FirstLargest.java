package comparisons;

public class FirstLargest {

    public static <T extends Comparable<T>> boolean isFirstLargest(T item, T item2, T item3)
    {
        if(item.compareTo(item2) > 0 && item.compareTo(item3) > 0)
        {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {

        int item1 = 5;
        int item2 = 2;
        int item3 = 2;

        System.out.println(isFirstLargest(item1,item2,item3));
    }
}
