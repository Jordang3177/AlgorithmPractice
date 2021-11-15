import java.util.Stack;

public class LargestPrimeFactor {
    public static void main(String[] args) {
        LargestPrimeFactor obj = new LargestPrimeFactor();
        long answer = obj.function(600851475143L);
        System.out.println(answer);
    }

    private Long function(long  x) {
        long answer = 0;
        for(int i = 2; i <= x; i++) {
            if(x%i == 0) {
                while(x%i == 0) {
                    answer = i;
                    x /= i;
                }
            }
        }
        return answer;
    }
}
