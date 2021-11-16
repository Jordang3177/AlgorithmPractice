import java.math.BigInteger;

public class Problem020 {
    public static void main(String[] args) {
        Problem020 obj = new Problem020();
        long firstTest = obj.FactorialDigitSum(10);
        System.out.println(firstTest);
        long secondTest = obj.FactorialDigitSum(100);
        System.out.println(secondTest);
    }

    private long FactorialDigitSum(int limit) {
        long answer = 0;
        BigInteger factorial = Factorial(limit);
        String bigNum = factorial.toString();
        for(int i = 0; i < bigNum.length(); i++) {
            answer += bigNum.charAt(i) - '0';
        }
        return answer;
    }

    private BigInteger Factorial(int num) {
        BigInteger answer = BigInteger.ONE;
        if(num == 0) {
            return BigInteger.ZERO;
        }
        for(int i = 1; i < num + 1; i++) {
            answer = answer.multiply(BigInteger.valueOf(i));
        }
        return answer;
    }
}
