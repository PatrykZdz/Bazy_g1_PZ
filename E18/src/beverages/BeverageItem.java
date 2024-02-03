package beverages;

public class BeverageItem implements Comparable<BeverageItem>{

    private String name;
    private double volume;
    private double sugarContent;

    public BeverageItem(String name, double volume, double sugarContent) {
        this.name = name;
        this.volume = volume;
        this.sugarContent = sugarContent;
    }

    @Override
    public String toString() {
        return "BeverageItem{" +
                "name='" + name + '\'' +
                ", volume=" + volume +
                ", sugarContent=" + sugarContent +
                '}';
    }

    @Override
    public int compareTo(BeverageItem o) {
        return Double.compare(this.sugarContent,o.sugarContent);
    }
}
