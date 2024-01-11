package zad1;
//import zad1.Person;
public class Main {
    public static void main(String[] args) {
        //zad1.Person
        Person p1 = new Person("Stefan", -1);
        System.out.println(p1.imie() + " " + p1.wiek());
    }
}
package zad1;

public record Person(String imie, int wiek) {
    public Person {
        if(wiek < 0){
            wiek = 0;
        }
    }
}
package zad2;

public class BenzynowySilnik implements Silnik{
    @Override
    public void start() {
        System.out.println("Uruchomiono silnik benzynowy");
    }
    @Override
    public void stop() {
        System.out.println("Zatrzymano silnik benzynowy");
    }
}
package zad2;

public class Main {
    public static void main(String[] args) {
        Silnik silnik = new BenzynowySilnik();
        Samochod samochod = new Samochod(silnik);
        samochod.start();
        samochod.stop();
    }
}
package zad2;

public class Samochod {
    private final Silnik silnik;
    public Samochod(Silnik silnik) {
        this.silnik = silnik;
    }
    public void start() {
        silnik.start();
    }
    public void stop() {
        silnik.stop();
    }
}
package zad2;

public interface Silnik {
    void start();
    void stop();
}
package zad3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Music implements Comparable<Music>{
    String title;
    String artist;
    int releaseYear;
    public Music(String title, String artist, int releaseYear) {
        this.title = title;
        this.artist = artist;
        this.releaseYear = releaseYear;
    }
    @Override
    public int compareTo(Music o) {
        return Integer.compare(o.releaseYear, releaseYear);
    }
    @Override
    public String toString(){
        return ""+releaseYear;
    }
    public static void main(String[] args){
        Music m1 = new Music("A", "A", 2000);
        Music m2 = new Music("B", "B", 2001);
        Music m3 = new Music("C", "C", 1993);
        Music m4 = new Music("B", "B", 2007);
        ArrayList<Music> MusicList = new ArrayList<>(Arrays.asList(m1, m2, m3, m4));
        for(var item : MusicList){
            System.out.println(item);
        }
        //Collections.sort(MusicList);
        MusicList.sort(new MusicComparator().reversed());
        System.out.println();
        for(var item : MusicList){
            System.out.println(item);
        }
    }
}
package zad3;

import java.util.Comparator;

public class MusicComparator implements Comparator<Music> {
    @Override
    public int compare(Music o1, Music o2) {
        return Integer.compare(o1.releaseYear, o2.releaseYear);
    }
}
package zad4;

import java.util.Date;

public class VideoGame implements Cloneable{
    private String title;
    private String genre;
    private Date releaseDate;
    public VideoGame(String title, String genre, Date releaseDate) {
        this.title = title;
        this.genre = genre;
        this.releaseDate = releaseDate;
    }
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public String getGenre() {
        return genre;
    }
    public void setGenre(String genre) {
        this.genre = genre;
    }
    public Date getReleaseDate() {
        return releaseDate;
    }
    public void setReleaseDate(Date releaseDate) {
        this.releaseDate = releaseDate;
    }
    @Override
    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
    public static void main(String[] args) {
        Date data = new Date(53, 1, 12);
        VideoGame game = new VideoGame("CS2", "Shooter", data);
        System.out.println(game.toString());
        try{
            VideoGame otherGame = (VideoGame) game.clone();
            Date oData = new Date(133, 2, 4);
            game.setReleaseDate(oData);
            System.out.println(game.toString());
            System.out.println(otherGame.toString());;
        } catch(CloneNotSupportedException e){
            throw new RuntimeException(e);
        }
    }
}
package zad5;

public class DoubleElement<T>{
    public T left;
    public T right;
}
package zad5;

public class Person {

}
class Student extends Person{

}
package zad5;

public class Person {

}
class Student extends Person{

}
package zad6;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean run = true;
        while(run) {
            try {
                System.out.println("Podaj a: ");
                int a = scanner.nextInt();
                System.out.println("Podaj b: ");
                int b = scanner.nextInt();
                int c = a / b;
                System.out.println(c);
                run = false;
            } catch (InputMismatchException e) {
                System.out.println("Oczekuje liczb całkowitych");
                scanner.nextLine();
            } catch (ArithmeticException e){
                System.out.println("Nie wolno dzielić przez 0");
                scanner.nextLine();
            }
        }
    }
}
