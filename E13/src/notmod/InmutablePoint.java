package notmod;

import java.util.Objects;

public final class InmutablePoint{

    private final int x;
    private final int y;
    private final int z;

    public InmutablePoint(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof InmutablePoint that)) return false;
        return x == that.x && y == that.y && z == that.z;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y, z);
    }

    @Override
    public String toString() {
        return "InmutablePoint{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                '}';
    }


}
