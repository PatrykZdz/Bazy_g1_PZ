package utilities;

public class PersonTest {
    public static void main(String[] args) {
        Person[] people = {new Person("Marek",20),
        new Person("Kuba",16),new Person("Jakub",17)};

        Person person1 = new Person("Anna",17);

        int count = Count.countLessThanOrEqual(people,person1);
        System.out.println(count);
    }
}
