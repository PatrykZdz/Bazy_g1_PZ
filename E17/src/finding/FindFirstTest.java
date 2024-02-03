package finding;

public class FindFirstTest {
    public static void main(String[] args) {

        String[] strings = {null, null, "Hello", null, "World"};
        Integer[] integers = {null, null, 3, null, 7};

        String firstNonNullString = FindFirst.findFirstNonNUll(strings);
        Integer firstNonNullInteger = FindFirst.findFirstNonNUll(integers);

        System.out.println("First non-null string: " + firstNonNullString);
        System.out.println("First non-null integer: " + firstNonNullInteger);
    }
}
