import java.math.BigInteger;

public class Problem016 {
    public static void main(String[] args) {
        Problem016 obj = new Problem016();
        BigInteger firstTest = obj.PowerDigitSum(15);
        System.out.println(firstTest);
        BigInteger secondTest = obj.PowerDigitSum(1000);
        System.out.println(secondTest);
    }

    private BigInteger PowerDigitSum(long pow) {
        BigInteger powers = BigInteger.TWO;
        for(int i = 2; i <= pow; i++) {
            powers = powers.multiply(BigInteger.TWO);
        }
        String numString = powers.toString();
        BigInteger answer = BigInteger.ZERO;
        for(int i = 0; i < numString.length(); i++) {
            answer = answer.add(BigInteger.valueOf(numString.charAt(i) - '0'));
        }
        return answer;
    }
}
