package music;

import java.util.ArrayList;
import java.util.Objects;

public class VinylStore extends MusicStore{

    private int numberOfVinyls;

    public VinylStore(String name, String city, int numberOfVinyls) {
        super(name, city);
        this.numberOfVinyls = numberOfVinyls;
    }

    public int getNumberOfVinyls() {
        return numberOfVinyls;
    }

    public void setNumberOfVinyls(int numberOfVinyls) {
        this.numberOfVinyls = numberOfVinyls;
    }

    @Override
    public String toString() {
        return "VinylStore{" + "name " + getName() +
                "City: " + getCity() + "Albums: " + getAlbums() +
                " numberOfVinyls=" + numberOfVinyls +
                '}';
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof VinylStore that)) return false;
        if (!super.equals(object)) return false;
        return numberOfVinyls == that.numberOfVinyls;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), numberOfVinyls);
    }
}

