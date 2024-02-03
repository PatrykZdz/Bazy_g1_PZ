package university;

import java.util.Arrays;

public class StudentTest {
    public static void main(String[] args) {
        Student[]students = {new Student("Marek",4.5,2),
                new Student("Kuba", 5.5, 3),
        new Student("Stafam",3.0,5),
        new Student("Jakub",3.0,3)};

        Arrays.sort(students);

        for(int i = 0; i < students.length;i++)
        {
            System.out.println(students[i]);
        }
    }
}
