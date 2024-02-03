package algorithm;

public class TestItemManager {
    public static void main(String[] args) {
        ItemManger itemManger = new ItemManger();
        itemManger.addItem(10);
        itemManger.addItem(20);
        System.out.println(itemManger);
        System.out.println(itemManger.getItem(1));
        System.out.println(itemManger.getItemCount());

    }
}
