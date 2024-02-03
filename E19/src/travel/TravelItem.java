package travel;

public class TravelItem implements Comparable<TravelItem> {
    private String name;
    private double weight;
    private double volume;

    public TravelItem(String name, double weight, double volume) {
        this.name = name;
        this.weight = weight;
        this.volume = volume;
    }

    @Override
    public String toString() {
        return "TravelItem{" +
                "name='" + name + '\'' +
                ", weight=" + weight +
                ", volume=" + volume +
                '}';
    }
    @Override
    public int compareTo(TravelItem o) {
        return Double.compare(this.weight,o.weight);

    }
}
