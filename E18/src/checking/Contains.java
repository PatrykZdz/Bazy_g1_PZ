package checking;

public class Contains {
    public static <T> boolean containsDuplicates(T item1, T item2, T item3)
    {
        if(item1.equals(item2) || item1.equals(item3) || item2.equals(item3))
        {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {

        int item1 = 3;
        int item2 = 2;
        int item3 = 2;

        System.out.println(containsDuplicates(item1,item2,item3));
    }
}
