package algorithm;

import java.util.Objects;

public class Student  {
    private String name;
    private float grade;

    public Student(String name, float grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof Student student)) return false;
        return Float.compare(grade, student.grade) == 0 && Objects.equals(name, student.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, grade);
    }

    public static void main(String[] args) {
        Student student1 = new Student("Marek", 4.5F);
        Student student2 = new Student("Ewa", 4.5F);
        Student student3 = new Student("Janusz",5.0F);

        CompareThree compareThree = new CompareThree();

        boolean areEqual =  compareThree.compareThree(student1,student2,student3);
        System.out.println(areEqual);
    }


}
