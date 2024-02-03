package transport;

import java.util.ArrayList;
import java.util.List;

public class TestBusStation
{
    public static void main(String[] args) {

        BusStation b1 = new BusStation("Dworzec","Warszawa");

        b1.addBus("111");
        b1.addBus("205");
        b1.addBus("360");

        System.out.println(b1);

        b1.removeBus("111");
        System.out.println(b1);


        IntercityBusStation intercityBusStation1 = new IntercityBusStation("Bartek","Krakow",120);
        System.out.println(intercityBusStation1);

        intercityBusStation1.addBus("120");
        intercityBusStation1.addBus("150");
        intercityBusStation1.addBus("300");
        intercityBusStation1.addBus("405");
        System.out.println(intercityBusStation1);

        intercityBusStation1.removeBus("405");
        intercityBusStation1.removeBus("300");
        System.out.println(intercityBusStation1);

    }
}
