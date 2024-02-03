package algorithm;

import java.nio.file.attribute.FileAttribute;
import java.util.TreeMap;

public class CompareThree {

    public static <T> boolean compareThree(T a, T b, T c) {
        if (a.equals(b) && a.equals(c))
        {
            if (b.equals(a) && b.equals(c))
            {
                if (c.equals(a) && c.equals(b))
                {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {

        String str1 = "abc";
        String str2 = "abc";
        String str3 = "abc";

        boolean resultStr = compareThree(str1, str2, str3);
        System.out.println("Czy wszystkie trzy napisy są równe? " + resultStr);

        Integer num1 = 42;
        Integer num2 = 42;
        Integer num3 = 42;

        boolean resultNum = compareThree(num1, num2, num3);
        System.out.println("Czy wszystkie trzy liczby są równe? " + resultNum);

        // Przykład z różnymi wartościami
        String differentStr = "xyz";
        boolean resultDifferent = compareThree(str1, str2, differentStr);
        System.out.println("Czy wszystkie trzy napisy są równe? " + resultDifferent);
    }
}

