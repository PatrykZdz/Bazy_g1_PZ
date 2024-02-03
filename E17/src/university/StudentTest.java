package university;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StudentTest {

    public static void main(String[] args) {

        List<Student> lista = new ArrayList<>();
        lista.add(new Student(5,"Zbyszek",4.25));
        lista.add(new Student(7,"Zbyszek",2.25));
        lista.add(new Student(3,"Zbyszek",2.25));
        lista.add(new Student(2,"Zbyszek",3.25));
        lista.add(new Student(1,"Zbyszek",7.25));

        Collections.sort(lista,new AverageGradeComparator().thenComparing(new IdComparator()));

        for(int i = 0; i < lista.size();i++) {
            System.out.println(lista.get(i));
        }
    }
}
