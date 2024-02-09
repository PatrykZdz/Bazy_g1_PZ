package ocean;

public final class ImmutableSubmarinePosition {
    private final double x;
    private final double y;
    private final double z;

    public ImmutableSubmarinePosition(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getZ() {
        return z;
    }

    @Override
    public String toString() {
        return "ImmutableSubmarinePosition{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                '}';
    }

    public ImmutableSubmarinePosition move(double xChange, double yChange, double zChange)
    {
        return new ImmutableSubmarinePosition(x+xChange,y+yChange,z+zChange);

    }


}
