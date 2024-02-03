package algorithm;

import java.util.HashMap;

public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }
    public static void main(String[] args) {
        // Przykładowe użycie dla klasy Person z polem name
        HashMap<Person, String> personMap = new HashMap<>();
        personMap.put(new Person("John"), "Data1");
        personMap.put(new Person("Alice"), "Data2");
        personMap.put(new Person("John"), "Data3"); // Ten klucz zostanie nadpisany, ponieważ jest równy kluczowi pierwszemu John

        int uniqueKeysCount = Count.countUniqueKeys(personMap);
        System.out.println("Liczba unikalnych kluczy w mapie: " + uniqueKeysCount);
}}
