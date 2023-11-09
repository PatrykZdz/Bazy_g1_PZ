public class Main {
    public static void main(String[] args) {
        //zad1();
        //zad2();
        //zad3();
        //zad4();
        //zad5();
        //zad6();
        zad7();
    }
    public static void zad1(){
        Cat kot = new Cat();
        kot.makeSound();
        //Animal zwierze = kot;
        Animal zwierze = new Cat();
        zwierze.makeSound();
        System.out.println(kot.imie);
    }
    public static void zad2(){
        Employee pracownik = new Employee();
        System.out.println(pracownik.displayData());
    }
    public static void zad3(){
        Hammer mlotek = new Hammer("hammer");
        System.out.println(mlotek.name);
    }
    public static void zad4(){
        Samochod samochod = new Samochod();
        samochod.jedz();
    }
    public static void zad5(){
        KalkulatorRozszerzony kalkR = new KalkulatorRozszerzony();
        System.out.println(kalkR.dodaj(1, 2, 3));
    }
    public static void zad6(){
        Laptop la = new Laptop();
        la.uruchom();
    }
    public static void zad7(){
        Programista pr = new Programista();
    }
}


public class Istota {
    public Istota(){
        System.out.println("Stworzono istote");
    }
}
class Czlowiek extends Istota{
    public Czlowiek(){
        System.out.println("Stworzono czlowieka");
    }
}
class Programista extends Czlowiek{
    public Programista(){
        System.out.println("Stworzono programiste");
    }
}


public class Komputer {
    public void uruchom(){
        System.out.println("Komputer uruchiomiony");
    }
}
class Laptop extends Komputer{
    @Override
    //protected nie działa bo w Komputer jest public
    public void uruchom(){
        System.out.println("Laptop jest uruchomiony");
    }
}

public class Kalkulator {
    public int dodaj(int a, int b){
        return a+b;
    }
}
class KalkulatorRozszerzony extends Kalkulator{
    public int dodaj(int a, int b, int c){
        return a+b+c;
    }
}

public class Kalkulator {
    public int dodaj(int a, int b){
        return a+b;
    }
}
class KalkulatorRozszerzony extends Kalkulator{
    public int dodaj(int a, int b, int c){
        return a+b+c;
    }
}

public class Tool {
    protected String name;
    protected Tool(String name) {
        this.name = name;
    }
}
class Hammer extends Tool{
    public Hammer(String name) {
        super(name);
    }
}

//final nie odziedziczalna
public class Animal {
    public String imie;
    public Animal(){
        this.imie = "Zwierze";
    }
    public Animal(String imie){
        this.imie = imie;
    }
    public void makeSound(){
        System.out.println("Generic animal noises");
    }
}
class Cat extends Animal{
    @Override
    public void makeSound(){
        //super.makeSound();
        System.out.println("Miau miau");
    }
}


public class Person {
    private static String firstName;
    protected static String lastName;
    public Person(){
        this.firstName = "default";
        this.lastName = "default";
    }
    public String getFirstName(){
        return firstName;
    }
    public String getLastName(){
        return lastName;
    }
}
class Employee extends Person{
    public String displayData(){
        return getFirstName() + ' ' + getLastName();
    }
}
