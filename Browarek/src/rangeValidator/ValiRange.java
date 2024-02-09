package rangeValidator;

public class ValiRange {

    public static <T extends Comparable<T>> void validateRange(T value, T min, T max)
    {
        if(value == null || min == null || max == null)
        {
            throw new IllegalArgumentException( );
        }
        if(value.compareTo(max) <= 0 && value.compareTo(min) >= 0)
        {
            System.out.println("Wartosc jest w zakresie");
        }
        else
        {

        }

    }

}
