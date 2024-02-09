package ocean;

public class TestImmutableSubmarinePosition {
    public static void main(String[] args) {

        ImmutableSubmarinePosition immutableSubmarinePosition1 = new ImmutableSubmarinePosition(12.0,13.9,15.0);

        System.out.println(immutableSubmarinePosition1);

        ImmutableSubmarinePosition immutableSubmarinePosition2 = immutableSubmarinePosition1.move(1,2,3);

        System.out.println(immutableSubmarinePosition2);

    }

}
