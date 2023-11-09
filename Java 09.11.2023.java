
public class Main {
    public static void main(String[] args) {

        Animal animal = new Animal("Zebra");
        Animal animal2 = new Animal("Zebra");
        System.out.println(animal == animal2);
        System.out.println(animal.equals(animal2));
        animal.makeNoise();
        Cat kot = new Cat("Filemon");
        System.out.println(kot.name);
        kot.makeNoise();
        Animal animal3 = new Cat("Bonifacy");
        animal3.makeNoise();
        System.out.println("");
        System.out.println("Zad 1");
        Employee pracownik = new Employee();
        System.out.println(pracownik.displayData());
        System.out.println("Zad 2");
        Hammer tool1 = new Hammer("Młotek");
        System.out.println(tool1.name);

        System.out.println("Zad 3");
        Book b = new Book("1","1",1);
        Book b2 = new Book("1","1",1);
        System.out.println(b);
        System.out.println(b.equals(b2));
        b2.numberOfPages = 3;
        System.out.println(b.equals(b2));

        Samochod s = new Samochod("Opel");
        s.jedz();

        }
    }



public class Kalkulator {
    public int dodaj(int a, int b){
        return a+b;

    }
}
class KalkulatorRozszerzony extends Kalkulator{
    public int dodaj(int a, int b, int c)
    {
        return a+b+c;
    }
}


public class Book {
    public String title;
    public String author;
    public int numberOfPages;

    public Book(String title, String author, int numberOfPages){
        this.numberOfPages = (numberOfPages >= 0) ? numberOfPages : 1;  /// to if lepiej jak nie ogarne
        this.title = (title == null || title.isEmpty()) ? "" : title;
        this.author = (author == null || author.isEmpty()) ? "" : author;
    }
    @Override
    public String toString () {
        return "Book: " +this.title+" by "+ this.author + " Pages: "+ this.numberOfPages ;

    }
    @Override
    public boolean equals (Object obj){ //objekt
        if (obj instanceof Book o) { // sprawdzenie czy(object) obj jest tego samego typu (object) Book o
            boolean pages = this.numberOfPages == o.numberOfPages;
            boolean author = this.author.equals(o.author);
            boolean title = this.title.equals(o.title);
            return pages && author && title;
        }
        else
        {
            return false;
        }
    }
}


public class Tool {
    protected String name;
    protected Tool(String name){
        this.name = name;
    }
}
class Hammer extends Tool{
    public Hammer(String name) {
        super(name);
    }
}

public class Pojazd {
    public void jedz(){
        System.out.println("Pojazd jedzie");
    }
}
class Samochod extends Pojazd{
    public String marka;
    public Samochod(String marka) {
        this.marka = marka;
    }
    @Override
    public void jedz() {
        super.jedz();
        System.out.println("Marka: " + this.marka);
    }
}


public class Person {
    private String firstName;
    protected String lastName;

    public Person(){
        this.firstName = "Anna";
        this.lastName = "Nowicka";
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
        return getFirstName()+" " + getLastName();
    }
}


public class Animal {
    public String name;
    public  Animal(){
        name = "default";
    }
    public Animal(String name){
        this.name=name;
    }
    @Override
    public String toString(){
        return this.name;
    }
    @Override
    public boolean equals(Object other) //Metoda
    {
        if (other instanceof Animal temp) {

            return this.name.equals(temp.name);
        }
        else{
            return false;
        }
    }
    public void makeNoise()
    {
        System.out.println("Odgłosy zwierzęcia");
    }
}
class Cat extends Animal{
    public Cat(){

    }

    public Cat(String name)// Konstruktor
    {
        super(name);
    }
    @Override // nadrzednosc
    public void makeNoise(){ // metoda
        System.out.println("Miau Miau");
    }
}

public class Komputer {
    public void uruchom() {
        System.out.println("Komputer uruchomiony");
    }

    class Laptop extends Komputer {
        @Override
        /*protected*/public void uruchom() {
            System.out.println("Laptop uruchomiony");
        }
    }
}

