package algorithm;

import java.util.HashMap;

import static algorithm.Mapa.mapToString;

public class Person {
    private String name;

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                '}';
    }

    public Person(String name) {
        this.name = name;
    }

    public static void main(String[] args) {

        HashMap<Object, Object> personMap = new HashMap<>();
        personMap.put(new Person("Alice"),1);
        personMap.put(new Person("Alice"), 2);
        personMap.put(new Person("Bob"), 3);

        String result = mapToString(personMap);
        System.out.println(result);
    }
}
