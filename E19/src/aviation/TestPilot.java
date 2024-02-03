package aviation;

import java.util.ArrayList;
import java.util.List;

public class TestPilot {
    public static void main(String[] args) {

        List<Double> lista = new ArrayList<>();
        lista.add(1.2);
        lista.add(2.3);
        lista.add(3.5);
        Pilot pilot = new Pilot("Pilot1",lista);

        System.out.println(pilot);

        pilot.setFlightHours(2,10.25);
        Pilot pilot2 = pilot.clone();
        System.out.println(pilot2);
    }
}
