package algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Index {

    public static <T> T atIndex(Iterator<T> iterator, int index)
    {

        if (index < 0) {
            throw new IllegalArgumentException("Index must be non-negative");
        }

        int currentIndex = 0;
        while (iterator.hasNext()) {
            T element = iterator.next();
            if (currentIndex == index) {
                return element;
            }
            currentIndex++;
        }

        throw new IndexOutOfBoundsException("Index " + index + " is out of bounds");
    }

    public static void main(String[] args) {
        List<String> stringList = new ArrayList<>(Arrays.asList("A", "B", "C", "D", "E"));

        Iterator<String> iterator = stringList.iterator();
        int indexToRetrieve = 2;

        try {
            String result = atIndex(iterator, indexToRetrieve);
            System.out.println("Element at index " + indexToRetrieve + ": " + result);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Index out of bounds");
        }
    }
}



