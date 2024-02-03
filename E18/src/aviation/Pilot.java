package aviation;

public class Pilot implements Cloneable {
    private String name;
    private double[] flightHours;

    public Pilot(String name, double[] flightHours) {
        this.name = name;
        this.flightHours = flightHours;
    }

    // Getter i setter dla name

    public double[] getFlightHours() {
        return flightHours.clone(); // Zapewnienie głębokiego kopiowania tablicy
    }

    public void setFlightHours(int index, double hours) {
        if (index >= 0 && index < flightHours.length) {
            flightHours[index] = hours;
        }
    }

    @Override
    public Pilot clone() {
        try {
            Pilot clonedPilot = (Pilot) super.clone();
            // Głębokie kopiowanie tablicy flightHours
            clonedPilot.flightHours = flightHours.clone();
            return clonedPilot;
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
            return null;
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
