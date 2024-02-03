package university;

public record Student(String name, double averageGrade,int yearOfStudy) implements Comparable<Student> {

    @Override
    /// compare (this.age, o.age)
    /// compareTo (o1.age, o2.age)
    public int compareTo(Student o) {
       int wynik = Double.compare(o.averageGrade,this.averageGrade);
       if(wynik == 0)
       {
           return Integer.compare(this.yearOfStudy,o.yearOfStudy);
       }
       return wynik;
    }
}
