package aviation;

import java.util.Arrays;

public class TestPilot {
    public static void main(String[] args) {
        double[] originalFlightHours = {10.5, 20.3, 15.2, 30.0, 25.5};
        Pilot originalPilot = new Pilot("John", originalFlightHours);

        // Klonowanie pilota
        Pilot clonedPilot = originalPilot.clone();

        // Zmiana liczby godzin lotu w oryginalnym pilocie
        originalPilot.setFlightHours(2, 18.0);

        // Wyświetlanie informacji
        System.out.println("Original Pilot - Name: " + originalPilot.getName());
        System.out.println("Original Pilot - Flight Hours: " + Arrays.toString(originalPilot.getFlightHours()));

        System.out.println("Cloned Pilot - Name: " + clonedPilot.getName());
        System.out.println("Cloned Pilot - Flight Hours: " + Arrays.toString(clonedPilot.getFlightHours()));
    }
}
