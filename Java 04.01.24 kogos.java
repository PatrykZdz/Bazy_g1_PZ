public class Main {
    public static void main(String[] args) {
        Box<Integer> box = new Box<>(3);
        //zad2();
        //zad3();
    }
    public static void zad2() {
        Counter<String> counter = new Counter<>();
        counter.add("Test");
        counter.add("Kolejny");
        counter.add("Nastepny");
        System.out.println(counter.getCount());
    }
    public static void zad3(){
    Triple<Integer, Double, String> triple = new Triple<>(1, 2.2, "Tekst");
        System.out.println(triple.getFirst());
        System.out.println(triple.getSecond());
        System.out.println(triple.getThird());
    }
    //public static <T extends Animal> T;
    //TODO: Stwórz klasę generyczną Pair<T>, która przechowuje dwa obiekty tego samego typu. Następnie utwórz dwie klasy: Plant i Tree, gdzie Tree dziedziczy po Plant. Klasa Tree powinna posiadać prywatne pole height, którego nie posiada klasa Plant. Następnie napisz statyczną metodę generyczną findMinMaxHeight, która przyjmuje jako argument tablicę obiektów typu Tree oraz Pair<? super Tree> result. Metoda powinna zapisać (jako obiekty typu Tree) najniższe i najwyższe (pod kątem wysokości) drzewo z tablicy w drugim argumencie metody. Wykorzystaj też generyczny interfejs Comparable.
    public static <T> void findMinMaxHeight(Tree[], Pair<? super Tree>){

    }
}

public class Plant {
}
class Tree extends Plant{
    private int height;
}

public class Pair <T>{
    T obj1;
    T obj2;
}

//TODO: Utwórz dwie klasy: Animal (Zwierzę) i Dog (Pies), gdzie Dog dziedziczy po Animal. Następnie napisz statyczną metodę generyczną findMax, która przyjmuje dwa argumenty: element1 i element2 typu extends Animal. Metoda powinna zwracać element większy według własnie zdefiniowanego kryterium porównania. W implementacji porównaj elementy bazując na wybranym przez siebie atrybucie, na przykład wieku.
public class Animal {
}
class Dog extends Animal{
}


//TODO: Napisz statyczną metodę generyczną minValue, która przyjmuje tablicę elementów typu generycznego T, gdzie T rozszerza Comparable<T>. Metoda powinna zwracać najmniejszy element z tablicy. Przetestuj tę metodę na tablicach zawierających różne typy porównywalnych obiektów, takie jak Integer, Double, czy String. Zabezpiecz metodę tak, aby nie można było jej wywołać z tablicą o zerowej liczbie elementów. Dodaj klasę ’Personz polaminameiagei przetestuj metodęminValuena tablicy obiektówPerson`.
public class Value {
    public static <T extends Comparable<T>> T minValue(T[] a) {
        if(a.length == 0 ) throw new IllegalArgumentException();
        T min = a[0];
        for(int i = 1; i < a.length; ++i){
            if(min.compareTo(a[i]) > 0) {
                min = a[i];
            }
        }
        return min;
    }
}

import java.util.Arrays;
//TODO: Zabezpiecz metodę tak, aby nie można było wywołać błędu związanego z przekroczeniem zakresu tablicy.
public class Swap {
    public static <T> void swap(T[] array, int a, int b) {
        T tmp1 = array[a];
        T tmp2 = array[b];
        array[a] = tmp2;
        array[b] = tmp1;
    }
    public static void main(String[] args) {
        Integer[] myArray = {0, 1, 2, 3, 4, 5, 6};
        swap(myArray, 0, 4);
        System.out.println(Arrays.toString(myArray));
    }
}

public class Equals{
    public static <T> boolean isEqual(T value1, T value2){
        return value1.equals(value2);
    }
    public static void main(String[] args){
        int a = 5;
        int b = 4;
        String s1 = "test";
        String s2 = "test";
        System.out.println(isEqual(a, b));
        System.out.println(isEqual(s1, s2));
    }
}

import java.util.ArrayList;
import java.util.List;

public class Counter <T>{
    public T element;
    List<T> list = new ArrayList<>();
    public void add(T element) {
        list.add(element);
    }
    public int getCount(){
        return list.size();
    }
}

public class Triple <T, U, V>{
    public T first;
    public U second;
    public V third;
    public Triple(T first, U second, V third) {
        this.first = first;
        this.second = second;
        this.third = third;
    }
    public T getFirst() {
        return first;
    }
    public U getSecond() {
        return second;
    }
    public V getThird() {
        return third;
    }
}


public class Box <T>{
    public T value;
    public Box(T value){
        this.value=value;
    }
    public T getValue(){
        return value;
    }
    public void setValue(T value){
        this.value = value;
    }
}


