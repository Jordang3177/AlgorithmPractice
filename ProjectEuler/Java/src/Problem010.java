import java.util.ArrayList;
import java.util.List;

public class Problem010 {
    public static void main(String[] args) {
        Problem010 obj = new Problem010();
        System.out.println(obj.SumOfPrimes(2000000));
    }

    public long SumOfPrimes(int limit) {
        List<Integer> primes = new ArrayList<>();
        primes.add(2);
        long answer = 2;
        for(int i = 3; i < limit; i+=2) {
            boolean isPrime = true;
            for(int prime : primes) {
                if(i % prime == 0) {
                    isPrime = false;
                    break;
                }
            }
            if(isPrime) {
                primes.add(i);
                answer += i;
            }
        }
        return answer;
    }
}
