package beverages;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BeverageItemTest {

    public static void main(String[] args) {

        List<BeverageItem> lista = new ArrayList<>();
        lista.add(new BeverageItem("Name1",1.0,17.5));
        lista.add(new BeverageItem("Name1",1.0,12.5));
        lista.add(new BeverageItem("Name1",1.0,15.5));
        lista.add(new BeverageItem("Name1",1.0,10.5));

        Collections.sort(lista);

        for(int i = 0; i < lista.size();i++)
        {
            System.out.println(lista.get(i));
        }


    }
}
