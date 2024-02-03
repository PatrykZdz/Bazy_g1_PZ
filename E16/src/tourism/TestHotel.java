package tourism;

public class TestHotel {
    public static void main(String[] args) throws CloneNotSupportedException {

        Hotel hotel1 = new Hotel("Williams",200.00);
        Hotel hotel2clone = hotel1.clone();

        hotel1.setName("Marcin");

        System.out.println(hotel1);
        System.out.println(hotel2clone);



    }
}
