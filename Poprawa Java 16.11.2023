// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.

import com.sun.source.tree.ArrayAccessTree;

import java.util.ArrayList;
import java.util.List;
/// Taki poziom bedzie na kolowkium
public class Main {
    public static void main(String[] args)
    {
       int []tab1 = {1,2,3};
       int []tab2 = {4,5,6};

       System.out.println(mergeArrays(tab1,tab2));

    }
    public static ArrayList<Integer> mergeArrays(int[] tab1, int[] tab2)
    {
        ArrayList<Integer>lista = new ArrayList<>();
        for(int i = 0; i < tab1.length;i++)
        {
            lista.add(tab1[i]);
        }
        for(int i = 0; i < tab2.length;i++)
        {
            lista.add(tab2[i]);
        }
        return lista;
    }
}

/////////////////

public class Student {
    public String firstName;
    public String lastName;
    public String fieldOfStudy;


    public Student(String firstName, String lastName,String fieldOfStudy)
    {

        this.firstName = firstName;
        this.lastName = lastName;
        this.fieldOfStudy = fieldOfStudy;

    }

    public Student(String firstName, String lastName)
    {
        this(firstName,lastName,"unknown");

    }

}
/////////////////////

public class Vehicle {
    public String brand;
    public String model;


    public Vehicle(String brand, String model) {
        this.brand = brand;
        this.model = model;


    }
}
class Car extends Vehicle
{
    public int numberOfDoors;

    public Car(String brand, String model, int numberOfDoors)
    {
        super(brand,model); // to jest this.brand z Vehicle///
        this.numberOfDoors = numberOfDoors;

    }
}

///////////////

public class Vehicle2 {
    public void drive()
    {
        System.out.println("The vehicle is moving");
    }
}
class Car2 extends Vehicle2
{
    @Override
    public void drive()
    {
        super.drive(); /// wywola sie ta 1 metoda a tak tylko do 2 do drive
        System.out.println("To jest samochod");
    }
}

////////////////////

// Wazne kolokwium
public class Book {
    public String title;
    public String author;
    public int numberOfPages;
    @Override
    public String toString()
    {
        return "Book" + title + "by" +author + "Pages" + numberOfPages;
    }
    @Override
    public boolean equals(Object obj)
    {
        if(obj instanceof Book temp)
        {
            return this.title.equals(temp.title)&&(this.author.equals(temp.author)&& this.numberOfPages == temp.numberOfPages);
        }
        return false;
    }


}

//// Rano w czwartek konsutlacje 
///// mozna na teamsie o zadanie napisac jak ktos chce 

