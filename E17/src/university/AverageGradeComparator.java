package university;

import java.util.Comparator;

public class AverageGradeComparator implements Comparator<Student> {


    @Override
    public int compare(Student o1, Student o2) {
        //return Double.compare(o1.AverageGrade(),o2.AverageGrade()); // od najmniejszej do najwiekszej
        return Double.compare(o2.AverageGrade(),o1.AverageGrade());  //od najwiekszej do najmniejszej

    }
}
