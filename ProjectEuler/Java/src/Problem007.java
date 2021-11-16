import java.util.ArrayList;
import java.util.List;

public class Problem007 {
    public static void main(String[] args) {
        Problem007 obj = new Problem007();
        long firstTest = obj.findNthPrime(6);
        System.out.println(firstTest);
        long secondTest = obj.findNthPrime(10001);
        System.out.println(secondTest);
    }

    public long findNthPrime(int n) {
        List<Integer> primes = new ArrayList<>();
        primes.add(2);
        for(int i = 3; primes.size() < n; i += 2) {
            boolean isPrime = true;
            for(int prime : primes) {
                if(i % prime == 0) {
                    isPrime = false;
                }
            }
            if(isPrime) {
                primes.add(i);
            }
        }
        return primes.get(n - 1);
    }
}
