package transport;

import java.util.Objects;

public class IntercityBusStation extends BusStation{
    private int numberOfPlatforms;

    public IntercityBusStation(String name, String city, int numberOfPlatforms) {
        super(name, city);
        this.numberOfPlatforms = numberOfPlatforms;
    }


    public int getNumberOfPlatforms() {
        return numberOfPlatforms;
    }

    public void setNumberOfPlatforms(int numberOfPlatforms) {
        this.numberOfPlatforms = numberOfPlatforms;
    }

    @Override
    public String toString() {
        return "IntercityBusStation{" +
                "name='" + getName() + '\'' +
                ", city='" + getCity() + '\'' +
                ", buses=" + getBuses() +
                ", numberOfPlatforms=" + numberOfPlatforms +
                '}';
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof IntercityBusStation that)) return false;
        if (!super.equals(object)) return false;
        return numberOfPlatforms == that.numberOfPlatforms;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), numberOfPlatforms);
    }


}
