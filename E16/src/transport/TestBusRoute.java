package transport;

public class TestBusRoute {
    public static void main(String[] args) {
        BusRoute busRoute1 = new BusRoute("12345","A","C");
        BusRoute busRoute2 = new BusRoute("345","B","D");
        busRoute1.printDetails();
        busRoute2.printDetails();

        System.out.println(busRoute1.isLongRoute());
        System.out.println(busRoute2.isLongRoute());
    }
}
