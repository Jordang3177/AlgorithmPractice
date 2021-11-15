import java.util.ArrayList;
import java.util.List;

public class EvenFibNumbers {
    public static void main(String[] args) {
        System.out.println(EvenFib(4000000));
    }

    public static int EvenFib(int limit) {
        List<Integer> fib = new ArrayList<>();
        fib.add(1);
        fib.add(2);
        int sum = 2;
        for(int i = 2; i < limit; i++) {
            int value = fib.get(i - 2) + fib.get(i - 1);
            if(value > limit) {
                break;
            }
            else if(value % 2 == 0) {
                sum += value;
            }
            fib.add(value);
        }
        return sum;
    }
}
