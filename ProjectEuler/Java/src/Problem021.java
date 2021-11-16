public class Problem021 {
    public static void main(String[] args) {
        Problem021 obj = new Problem021();
        long firstTest = obj.AmicableNumbers(10000);
        System.out.println(firstTest);
    }

    private long AmicableNumbers(int limit) {
        long answer = 0;
        for(int i = 4; i < limit; i++) {
            long sumI = SumOfDivisors(i);
            if(i == SumOfDivisors(sumI) && i != sumI) {
                answer += i;
            }
        }
        return answer;
    }

    private long SumOfDivisors(long n) {
        long answer = 1;
        int end = (int) Math.pow(n, 0.5);
        for(int i = 2; i < end; i++) {
            if(n % i == 0) {
                answer += i;
                answer += n / i;
            }
        }
        if((long) end * end == n) {
            answer += end;
        }
        return answer;
    }
}
