package travel;

import java.util.Arrays;


public class TravelItemTest {
    public static void main(String[] args) {

        TravelItem[] travelItems ={new TravelItem("item1", 20.00, 1),
                new TravelItem("item1", 30.00, 1),
                new TravelItem("item1", 25.00, 1),
                new TravelItem("item1", 60.00, 1)};


        Arrays.sort(travelItems);

        for(int i= 0; i < travelItems.length;i++)
        {
            System.out.println(travelItems[i]);
        }

    }
}
