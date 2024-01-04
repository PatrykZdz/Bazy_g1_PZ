import Zad1.Box;

import java.util.Arrays;
/// Pakiety
public class Main {
    public static void main(String[] args)
    {
       Box<String,Integer> box1 = new Box<>("Cześć",6);
       Box<Integer,String> box2 = new Box<>(5,"napis");
       Box<Integer,Integer> box3 = new Box<>(4,5);

       wypisz(4);
       wypisz("Cześć");
       System.out.println(isEqual(5,"Cześć"));

       Triple<Integer,Integer,String> triple1 = new Triple<>(5,4,"kwiat");
       System.out.println(triple1.getFirst());
       System.out.println(triple1.getSecond());
       System.out.println(triple1.getThird());

        Integer[] myArray = {0,1,2,3,4,5,6};
        swap(myArray,0,4);
        System.out.println(Arrays.toString(myArray));

        String[] myArray2 = {"Kot","Pies"};
        System.out.println(maxvalue(myArray));
        System.out.println(maxvalue(myArray2));

        Float[] myArray3 = {1.43F, 3.54F};
        System.out.println(maxvalue(myArray3));

        Vehicle vehicle1 = new Vehicle("Skoda",120);



    }
    public static <T> void wypisz(T value)
    {
        System.out.println(value);
    }
    public static <T> boolean isEqual(T value1, T value2)
    {
        return value1.equals(value2);
    }
    public static <T> void swap(T[] tab,int a,int b)
    {

        try
        {
            T indeks1 =  tab[a];
            T indeks2 =  tab[b];
            tab[a] = indeks2;
            tab[b] = indeks1;
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Not swappable");
        }
    }
    public static <T extends Comparable<T>> T maxvalue(T[] tab)
    {
        if (tab.length == 0) throw new IllegalArgumentException();
        T max = tab[0];
        for(int x = 1; x < tab.length;x++)
        {
            if(max.compareTo(tab[x]) < 0)
            {
                max = tab[x];
            }
        }
        return max;
    }
}
public class Vehicle implements Comparable {
    public String model;
    public int speed;

    public Vehicle(String model, int speed) {
        this.model = model;
        this.speed = speed;
    }

    @Override
    public int compareTo(Object o)
    {
        return 0;
    }
}
public class Car {

}
class ElectricCar extends Car
{
    public static <T> boolean compareObjects(T object1, T object2)
    {

        return false;
    }

}
package Zad1;
/// Pakiety pod foldery i mozna przerzucac classy

public class Box <T,U> { // Klasy generyczne
    T value;
    U value2;

    public Box(T value, U value2) {
        this.value = value;
        this.value2 = value2;
    }

}
public class Triple <T,U,V> /// Dowolny typ
{
    T value;
    U value2;
    V value3;
    public Triple(T value, U value2, V value3)
    {
        this.value = value;
        this.value2 = value2;
        this.value3 = value3;
    }
    public T getFirst() {
        return value;
    }
    public U getSecond() {
        return value2;
    }
    public V getThird() {
        return value3;
    }
}
