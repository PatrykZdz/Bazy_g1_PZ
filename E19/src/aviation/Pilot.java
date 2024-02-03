package aviation;

import java.util.ArrayList;
import java.util.List;

public class Pilot implements Cloneable{

    private String name;
    private List<Double> flightHours;

    public Pilot(String name, List<Double> flightHours) {
        this.name = name;
        this.flightHours = new ArrayList<>(flightHours);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Double> getFlightHours() {
        return new ArrayList<>(flightHours);
    }


    public void setFlightHours(int index, double hours) {
        if (index >= 0 && index < flightHours.size()) {
            flightHours.set(index, hours);
        }
    }

    @Override
    public String toString() {
        return "Pilot{" +
                "name='" + name + '\'' +
                ", flightHours=" + flightHours +
                '}';
    }

    @Override
    public Pilot clone() {
        try {
            Pilot clone = (Pilot) super.clone();
            clone.flightHours = new ArrayList<>(this.flightHours);
            return clone;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
