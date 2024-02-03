package student;

public record StudentRecord(String name, String id, double gpa) {

    public StudentRecord(String name, String id, double gpa) {
            if(gpa >= 0.0 && gpa <= 4.0)
            {
                this.gpa = gpa;
                this.name = name;
                this.id = id;
            }
            else
            {
                throw new IllegalArgumentException("Nie jest w przedziale");
            }
    }
    public boolean isHonorStudent()
    {
        return gpa>=3.5;
    }
    public void printDetails()
    {
        System.out.println("Name: "+name+ "Id"+id+"GPA:"+ gpa);
    }
    // Metody dostępowe (getters) mogą być dodane, jeśli są potrzebne
    // Nie musza byc gdyz record ma bazowo je dodane
    // public String getName() {
    //     return name;
    // }

    // public String getId() {
    //     return id;
    // }

    // public double getGpa() {
    //     return gpa;
    // }

}
