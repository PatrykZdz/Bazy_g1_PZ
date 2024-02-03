package algorithm;

import java.util.ArrayList;
import java.util.List;

public class ClearTest {
    public static void main(String[] args) {

        // Testowanie dla kolekcji zawierającej element
        List<String> list1 = new ArrayList<>();
        list1.add("Hello");
        list1.add("World");

        System.out.println("Przed clearIfContains: " + list1);
        Clear.clearIfContains(list1, "Hello");
        System.out.println("Po clearIfContains: " + list1);


        // Testowanie dla kolekcji niezawierającej elementu
        java.util.List<String> list2 = new java.util.ArrayList<>();
        list2.add("Java");
        list2.add("Programming");

        System.out.println("Przed clearIfContains: " + list2);
        Clear.clearIfContains(list2, "Hello");
        System.out.println("Po clearIfContains: " + list2);
    }
}
