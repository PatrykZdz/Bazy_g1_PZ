package tourism;

public class Hotel implements Cloneable{
    private String name;
    private double capacity;

    public Hotel(String name, double capacity) {

        if(name == null)
        {
            this.name = "";
        }
        else
        {
            this.name= name;
        }
        if(capacity < 0)
        {
            this.capacity = 50.0;
        }
        else
        {
            this.capacity = capacity;
        }
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Hotel{" +
                "name='" + name + '\'' +
                ", capacity=" + capacity +
                '}';
    }

    @Override
    protected Hotel clone() throws CloneNotSupportedException {
        return (Hotel) super.clone();
    }
}
