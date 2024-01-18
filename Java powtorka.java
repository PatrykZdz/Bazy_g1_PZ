ZAD1
//// Najwaznijesze  RECORD Z Konstruktorem
package Zad1;
public record BankAccount(String numerKonta, double saldo) {
    public BankAccount(String numerKonta) { // Konstruktor
        this(numerKonta,0);

    }
}
/// Record z Metoda
package Zad1;
public record Car(String brand,String model, double fuelConsumptionPer100km) {

    public double fuelCost(double fuelPrice,double distance) /// Metoda
    {
        double fuelConsumed = (fuelConsumptionPer100km / 100) * distance;
        return fuelConsumed * fuelPrice;
    }
}
/// Record Address w Person
public record Person(String firstName, String lastName, Address adres) {

}

package Zad1;
public record Address(String street, int houseNumber, String postalCode, String city) {
}


/// Main
package Zad1;
public class Main {
    public static void main(String[] args) {

    ////Obiekty
        BookDT0 book1 = new BookDT0("Tytul1", "Autor1", 20.99,1999);
        BookDT0 book2 = new BookDT0("Tytul2","Autor2",21.99,2000);
        BookDT0 book3 = new BookDT0("Tytul3","Autor3",22.99,2015);


        Address adres1 = new Address("Mikojaki",56,"10-900","Warsaw");
        Person person1 = new Person("Adam","Rybak",adres1);

        System.out.println(book1);
        System.out.println(book2);
        System.out.println(book3);

        System.out.println(person1);


        BankAccount bankAccount1 = new BankAccount("123456789");
        System.out.println(bankAccount1);

        MusicTrack musicTrack1 = new MusicTrack("Title", "Unknown");
        System.out.println(musicTrack1);

        Car car1 = new Car("Opel","Astra",10.5);
        System.out.println(car1.fuelCost(7.50,300));

    }
}
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
ZAD2 Comparator i comparable
package Zad2;

import java.util.Comparator;

public class IdComparator implements Comparator<Student> {
    @Override
    public int compare(Student o1, Student o2) {
        return Integer.compare(o1.id, o2.id);
    }
}

package Zad2;

import java.time.LocalDate;

/// implements Comparable<nazwaKlasy> || prawy przycisk i metoda compareTo
public class Ksiazka implements Comparable<Ksiazka> {

    public String tytul;
    public int liczbaStron;
    public LocalDate dataWydania;

    public Ksiazka(String tytul, int liczbaStron, LocalDate dataWydania) {
        this.tytul = tytul;
        this.liczbaStron = liczbaStron;
        this.dataWydania = dataWydania;
    }

    @Override
    public String toString() {
        return "Ksiazka{" +
                "tytul='" + tytul + '\'' +
                ", liczbaStron=" + liczbaStron +
                ", dataWydania=" + dataWydania +
                '}';
    }

    @Override
    public int compareTo(Ksiazka o) {
        return Integer.compare(o.liczbaStron,this.liczbaStron); // Sortowanie wedlug stron malejaca
        //return Integer.compare(this.liczbaStron,o.liczbaStron); // Sortowanie wedlug stron rosnoca
    }
}


package Zad2;

import java.time.LocalDate;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        /// Tablica obiektow
        Ksiazka[] ksiazkas = {new Ksiazka("Książka1", 200, LocalDate.of(2020, 1, 1)),
                new Ksiazka("Książka2", 150, LocalDate.of(2019, 5, 15)),
                new Ksiazka("Książka3", 300, LocalDate.of(2022, 8, 20)),
                new Ksiazka("Książka4", 180, LocalDate.of(2021, 3, 10))
        };
        Arrays.sort(ksiazkas); // Sortowanie
        System.out.println("Posortowana Lista Malejąco:");
        for(int i = 0; i < ksiazkas.length;i++) // Wypisanie
        {
            System.out.println(ksiazkas[i]);
        }

        Samochod[] samochods = {new Samochod("Toyota", 50000, 2018),
                new Samochod("Ford", 70000, 2019),
                new Samochod("Volkswagen", 60000, 2020),
                new Samochod("BMW", 45000, 2017)};

        Arrays.sort(samochods);
        System.out.println();
        System.out.println("Posortowana Lista Rosnąco:");
        for(int i = 0; i < samochods.length;i++)
        {
            System.out.println(samochods[i]);
        }

        /// Lista Tablicowa
        List<Zamowienie> zamowienia = new ArrayList<>();
        zamowienia.add(new Zamowienie("Produkt1", 5, 25.0));
        zamowienia.add(new Zamowienie("Produkt2", 3, 30.0));
        zamowienia.add(new Zamowienie("Produkt3", 2, 25.0));
        zamowienia.add(new Zamowienie("Produkt4", 4, 20.0));

        zamowienia.sort(null);

        System.out.println();
        System.out.println("Posortowane malejąco według ceny jednostkowej, a przy równości sortowane były rosnąco według ilości");
        for(int i = 0; i < zamowienia.size();i++)
        {
            System.out.println(zamowienia.get(i));
        }


        List<Order> orders = new ArrayList<>();
        orders.add(new Order(1, "Customer1", LocalDate.of(2022, 1, 15)));
        orders.add(new Order(2, "Customer2", LocalDate.of(2022, 2, 20)));
        orders.add(new Order(3, "Customer3", LocalDate.of(2022, 1, 10)));
        orders.add(new Order(4, "Customer4", LocalDate.of(2022, 2, 5)));
        orders.add(new Order(5, "Customer5", LocalDate.of(2022, 1, 25)));


        Collections.sort(orders,new OrderComparator());////lub tak: orders.sort(new Order2());
        System.out.println();
        System.out.println("Posortowana Lista:");
        for(int i = 0; i < orders.size();i++)
        {
            System.out.println(orders.get(i));
        }


        Song[] songs ={new Song("Song1", "Artist1", 180),
                new Song("Song2", "Artist2", 220),
                new Song("Song3", "Artist3", 200),
                new Song("Song4", "Artist4", 180),
                new Song("Song5", "Artist5", 240)
        };

        Arrays.sort(songs,new SongComparator());
        System.out.println();
        System.out.println("Posortowana tablica:");
        for(int i = 0; i < songs.length;i++)
        {
            System.out.println(songs[i]);
        }


        List<Student> students = new ArrayList<>();
        students.add( new Student(1, "Student1", 4.5));
        students.add(new Student(2, "Student2", 3.8));
        students.add(new Student(3, "Student3", 4.2));
        students.add(new Student(5, "Student5", 4.8));
        students.add(new Student(4, "Student4", 4.0));

        Collections.sort(students,new AverageGradeComparator());
        System.out.println();
        for (int i = 0; i < students.size();i++)
        {
            System.out.println(students.get(i));
        }

        Collections.sort(students,new IdComparator());
        System.out.println();
        for (int i = 0; i < students.size();i++)
        {
            System.out.println(students.get(i));
        }

        /// NIE DOKONCA
        // Utwórz oryginalnego sportowca
       // Athlete originalAthlete = new Athlete("John Doe", List.of(60, 62, 58, 61, 59));

        // Sklonuj sportowca
       // Athlete clonedAthlete = originalAthlete.clone();

        // Zmiana czasu na pozycji 3 oryginalnego sportowca
       // originalAthlete.setLapTime(2, 55);


        // Wyświetl czasy obu sportowców
        //System.out.println("Oryginalny sportowiec: " + originalAthlete);
        //System.out.println("Sklonowany sportowiec: " + clonedAthlete);
    }


}

package Zad2;

import java.util.Comparator;

/// Comparator
public class OrderComparator implements Comparator<Order>  {
    @Override
    public int compare(Order o1, Order o2) {
        int dateComparation = o1.orderDate.compareTo(o2.orderDate);
        if (dateComparation == 0)
        {
            return Integer.compare(o1.id, o2.id);

        }
        return dateComparation;
    }
}

package Zad2;

public class Samochod implements Comparable<Samochod> {
    public String marka;
    public int przebieg;
    public int rokProdukcji;

    public Samochod(String marka, int przebieg, int rokProdukcji) {
        this.marka = marka;
        this.przebieg = przebieg;
        this.rokProdukcji = rokProdukcji;
    }

    @Override
    public String toString() {
        return "Samochod{" +
                "marka='" + marka + '\'' +
                ", przebieg=" + przebieg +
                ", rokProdukcji=" + rokProdukcji +
                '}';
    }

    @Override
    public int compareTo(Samochod o) {
        return Integer.compare(this.przebieg,o.przebieg); // Integer.compare( )
    }
}

package Zad2;

public class Song {
    public String title;
    public String artist;
    public int duration;

    public Song(String title, String artist, int duration) {
        this.title = title;
        this.artist = artist;
        this.duration = duration;
    }

    @Override
    public String toString() {
        return "Song{" +
                "title='" + title + '\'' +
                ", artist='" + artist + '\'' +
                ", duration=" + duration +
                '}';
    }


}

package Zad2;

import java.util.Comparator;

public class SongComparator implements Comparator<Song>{
    @Override
    public int compare(Song o1, Song o2) {
        int DurationComparation = Integer.compare(o1.duration,o2.duration);
        if(DurationComparation == 0)
        {
            return o1.title.compareTo(o2.title);
        }
        return DurationComparation;
    }
}

package Zad2;

public class Zamowienie implements Comparable<Zamowienie> {
    public String nazwaProduktu;
    public int ilosc;
    public double cenaJednostkowa;

    public Zamowienie(String nazwaProduktu, int ilosc, double cenaJednostkowa) {
        this.nazwaProduktu = nazwaProduktu;
        this.ilosc = ilosc;
        this.cenaJednostkowa = cenaJednostkowa;
    }

    @Override
    public String toString() {
        return "Zamowienie{" +
                "nazwaProduktu='" + nazwaProduktu + '\'' +
                ", ilosc=" + ilosc +
                ", cenaJednostkowa=" + cenaJednostkowa +
                '}';
    }

    @Override
    public int compareTo(Zamowienie o) {
        int comparePrice =  Double.compare(o.cenaJednostkowa,this.cenaJednostkowa);
        if(comparePrice == 0)
        {
            Integer.compare(this.ilosc,o.ilosc);
        }
        return comparePrice;
    }
}

////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
ZAD 3 Implentowanie wlasnych Interfaceow
package Zad3;

public interface MediaPlayer {
    /// Metody Abstrakcyjne
     void play(String trackName);
     void pause();
     String getCurrentTrack();

}

package Zad3;

public class AudioPlayer implements MediaPlayer{
    public String currentTrack;
    @Override
    public void play(String trackName) {
        System.out.println("Gra utwór: " + trackName );
        currentTrack = trackName;
    }

    @Override
    public void pause() {
        System.out.println("Zatrzymano");
    }

    @Override
    public String getCurrentTrack() {
        return currentTrack;
    }
}

package Zad3;

public class VideoPlayer implements MediaPlayer{

    public String current;
    @Override
    public void play(String trackName) {
        System.out.println("Leci film: "+trackName);
        current = trackName;
    }

    @Override
    public void pause() {
        System.out.println("Zatrzymano film:" + current);
    }

    @Override
    public String getCurrentTrack() {
        return current;
    }
}

package Zad3;

public class MediaPlayerTest {
    public static void main(String [] args)
    {
        AudioPlayer audioPlayer1 = new AudioPlayer();
        audioPlayer1.play("Eyes-Travis Scoot");
        audioPlayer1.pause();
        System.out.println(audioPlayer1.getCurrentTrack());

        System.out.println();
        VideoPlayer videoPlayer1= new VideoPlayer();
        videoPlayer1.play("Tenet");
        videoPlayer1.pause();
        System.out.println(videoPlayer1.getCurrentTrack());

    }

}

package Zad3;

public interface VehicleManager {
    String startEngine();
    int getFuelLevel();


}
package Zad3;

public class Motorcycle implements VehicleManager{
    @Override
    public String startEngine() {
        return "Silnik motocykle uruchomiony";
    }
    @Override
    public int getFuelLevel() {
        return 30;
    }
}

package Zad3;

public class Car implements VehicleManager {
    @Override
    public String startEngine() {
        return "Silnik samochodu uruchomiony";
    }
    @Override
    public int getFuelLevel() {
        return 50;
    }
}


package Zad3;

public class VehicleManagerTest {
    public static void main(String [] args)
    {
        Car car1 = new Car();
        System.out.println(car1.startEngine());
        System.out.println(car1.getFuelLevel());


        System.out.println();
        Motorcycle motorcycle1 = new Motorcycle();
        System.out.println(motorcycle1.startEngine());
        System.out.println(motorcycle1.getFuelLevel());
    }
}
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
ZAD 4

package Zad4;

public interface Printer {
    void drukuj(String tekst);
}


package Zad4;

public class Biuro {
    private Printer printer;  /// INterface jako zmienna

    public Biuro(Printer printer) {
        this.printer = printer;
    }
    public void drukujDokument(String tekst)
    {
        printer.drukuj(tekst);
    }
}
package Zad4;

public class StandardowyPrinter implements Printer{
    @Override
    public void drukuj(String tekst) {
        System.out.println(tekst);

    }
    public static void main(String[] args)
    {
        StandardowyPrinter standardowyPrinter1 = new StandardowyPrinter();// nie dajemy tak Interface
        standardowyPrinter1.drukuj("Drukuje");

        Biuro biuro = new Biuro(standardowyPrinter1);
        biuro.drukujDokument("To jest wazny dokument");

    }
}



package Zad4;
/// Dokonczyc 2 ostatnie
import java.util.Scanner;

public class Main_Z_Programami {
    public static void main(String[] args)
    {

        try {
            checkAge(20);
            checkAge(15);
            checkAge(25);
        }
        catch (IllegalArgumentException e) /// Obsluga wyjatku
        {
            /// Wyswieltli komunikat  Obsulga wyjatku
            System.out.println("Blad: " + e.getMessage());
            ///Wyslwietli na czerwono Wyrzucenie wyjatku
            ///throw new ArithmeticException("Dzielnie przez 0");
        }

    }
    public static void checkAge(int age) // Static
    {
        if (age < 18)
        {
            throw new IllegalArgumentException("Zbyt Młody");
            /// Wyrzucenie wyjatku
        }
        else
        {
            System.out.println(age);
        }
    }
}

package Zad4;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main_Z_Programami2 {

    public static void main (String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        while (true)
        {
        try {
            System.out.println("Podaj A: ");
            int a = scanner.nextInt();
            System.out.println("Podaj B: ");
            int b = scanner.nextInt();
            double wynik = dzielenie(a,b);
            System.out.println(wynik);
            break;

        }
        catch (InputMismatchException e)
        {
            System.out.println("Nie podano cyfry");
        }
        catch (ArithmeticException e)
        {
            System.out.println("Dzielenie przez zero nie jest dozwolone");
        }
        scanner.nextLine();
        }
    }
    public static double dzielenie(int liczba1, int liczba2)
    {
        if(liczba2 == 0)
        {
            throw new ArithmeticException("Dzielenie przez 0");
        }
        else
        {
            return (double) liczba1 /liczba2;
        }
    }
}

package Zad4;

public class NiepoprawnyFormatDanychException extends Exception{

    public NiepoprawnyFormatDanychException(String dane)
    {
        super(dane);
    }

    public static void main(String [] args)
    {
        try {
            SprawdzFormatDanych("niepoprawnyAdresEmail");
            System.out.println("Format danych jest poprawny.");
        } catch (NiepoprawnyFormatDanychException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    public static void SprawdzFormatDanych(String dane) throws NiepoprawnyFormatDanychException {

        if(!dane.matches("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}$"))
        {
            throw new NiepoprawnyFormatDanychException("Niepoprawny format danych");
        }

    }
}
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
ZAD 5 Generyczne
package Zad5;

public class Main1 {
    public static void main(String[] args)
    {
        int number1 = 43;
        int number2 = 65;
        System.out.println(isEqual(number1,number2));

        String tekst1 = "Hello";
        String tekst2 = "World";
        System.out.println(isEqual(tekst1,tekst2));

    }
    /// Metoda generyczna
    public static <T> boolean isEqual(T obj1, T obj2) /// Dowolny obiekt nawet bez posiadnia obiektu
    {
        return obj1.equals(obj2);

    }
}


package Zad5;

import java.util.Arrays;

public class Main2 {

    public static void main(String[] args)
    {
        try{
            Integer[] tab = {1,2,3,4}; // Tak musi byc
            swap(tab,0,6);
            System.out.println(Arrays.toString(tab));
        }
        catch (ArrayIndexOutOfBoundsException e)
        {
            System.out.println(e.getMessage());
        }


    }
    public static <T> void swap(T[] tab, int indeks1, int indeks2) {
        /// Nie jest potrzebne
        if (indeks1 < 0 || indeks1 >= tab.length || indeks2 < 0 || indeks2 >= tab.length) {
            throw new ArrayIndexOutOfBoundsException("Nieprawidłowe indeksy. Poza rozmiarem tablicy.");
        }

        T temp = tab[indeks1];
        tab[indeks1] = tab[indeks2];
        tab[indeks2] = temp;
    }
}


package Zad5;

public class Main3 {
    public static void main(String[] args)
    {
        Integer[] intTab = {5, 2, 8, 1, 9};
        Float[] floatTab = {2.5f, 7.2f, 4.8f, 1.3f};
        String[] stringTab = {"apple", "banana", "cherry", "date"};
        Vehicle[] vehicleTab =
                {
                        new Vehicle("Car", 120),
                        new Vehicle("Bike", 25),
                        new Vehicle("Truck", 80)
                };

        System.out.println("Max int tab: " + maxValue(intTab));
        System.out.println("Max float tab: " + maxValue(floatTab));
        System.out.println("Max string tab: " + maxValue(stringTab));
        System.out.println("Max speed w vehicle tab: " + maxValue(vehicleTab).getSpeed());
    }

    public static <T extends Comparable<T>> T maxValue (T[] tab)
    {
        if (tab.length == 0
        ) {
            throw new IllegalArgumentException("Tablica nie moze byc pusta");
        }

        T max = tab[0];
        for (T element : tab)
        {
            if (element.compareTo(max) > 0)
            {
                max = element;
            }
        }
        return max;
    }
    static class Vehicle implements Comparable<Vehicle>
    {
        private String model;
        private int speed;

        public Vehicle(String model, int speed)
        {
            this.model = model;
            this.speed = speed;
        }

        public int getSpeed()
        {
            return speed;
        }

        @Override
        public int compareTo(Vehicle other)
        {
            return Integer.compare(this.speed, other.speed);
        }
    }
}


package Zad5;

public class Triple <T,U,V>{

    T first;
    U second;
    V third;

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
    public static void main(String[] args) {
        Triple<String, Integer, Double> exampleTriple = new Triple<>("Hello", 42, 3.14);

        String firstElement = exampleTriple.getFirst();
        Integer secondElement = exampleTriple.getSecond();
        Double thirdElement = exampleTriple.getThird();

        System.out.println("First Element: " + firstElement);
        System.out.println("Second Element: " + secondElement);
        System.out.println("Third Element: " + thirdElement);
    }
}





