package rangeValidator;

public class ValiTest {

    public static void main(String[] args){
        int value = 10;
        int min = 5;
        int max = 15;

        ValiRange.validateRange(value,min,max);

        value = 20;
        ValiRange.validateRange(value,min,max);
    }
}
