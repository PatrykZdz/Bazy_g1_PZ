package utilities;

import java.util.ArrayList;

public class AppendFromEnd {
    public static <T> void appendFromEnd(ArrayList<? super T> destination, ArrayList<T> source) {
        int sourceSize = source.size();
        for (int i = sourceSize - 1; i >= 0; i--) {
            destination.add(source.get(i));

        }
    }

    public static void main(String[] args) {
        ArrayList<Object> destinationList = new ArrayList<>();
        ArrayList<Integer> sourceList = new ArrayList<>();

        sourceList.add(1);
        sourceList.add(2);
        sourceList.add(3);

        appendFromEnd(destinationList, sourceList);

        System.out.println("Zawartość docelowej listy po dodaniu z końca:");
        System.out.println(destinationList);
    }
}
