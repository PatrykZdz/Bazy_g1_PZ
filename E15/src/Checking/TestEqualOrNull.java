package Checking;

public class TestEqualOrNull {
    public static void main(String[] args)
    {
       int wynik = 5;
       int wynik2 = 5;
       String wynik3 = "Hello";
       String wynik4 = null;
       String wynik5 = null;

       System.out.println(EqualOrNull.isEqualOrNull(wynik,wynik2));
       System.out.println(EqualOrNull.isEqualOrNull(wynik,wynik3));
       System.out.println(EqualOrNull.isEqualOrNull(wynik4,wynik5));



    }
}
