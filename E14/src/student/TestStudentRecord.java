package student;

public class TestStudentRecord {
    public static void main(String[] args) {
        StudentRecord studentRecord1 = new StudentRecord("Marek","123",4.0);
        StudentRecord studentRecord2 = new StudentRecord("Kuba","234",1.0);

        studentRecord1.printDetails();
        studentRecord2.printDetails();
        System.out.println(studentRecord1.isHonorStudent());
    }
}
