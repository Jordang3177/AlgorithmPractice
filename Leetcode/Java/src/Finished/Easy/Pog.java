package Finished.Easy;

public class Pog {
    public static void main(String[] args) {
        Pog obj = new Pog();
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


[3,-2,3,4,5,6,-7,-36, 1,2, -1, 3,3]
 3, 1,4,8,13,19,12,-24
      3,7,12,18,25,-11