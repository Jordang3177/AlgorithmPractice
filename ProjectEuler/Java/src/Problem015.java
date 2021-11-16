import java.math.BigInteger;

public class Problem015 {
    public static void main(String[] args) {
        Problem015 obj = new Problem015();
        BigInteger firstTest = obj.LatticePaths(2);
        System.out.println(firstTest);
        BigInteger secondTest = obj.LatticePaths(3);
        System.out.println(secondTest);
        BigInteger thirdTest = obj.LatticePaths(20);
        System.out.println(thirdTest);
    }

    private BigInteger LatticePaths(int gridSize) {
        BigInteger top = Factorial(gridSize * 2);
        BigInteger bottom = Factorial(gridSize);
        bottom = bottom.multiply(bottom);
        BigInteger answer = top.divide(bottom);
        return answer;
    }

    private BigInteger Factorial(int num) {
        if(num == 0) {
            return BigInteger.ZERO;
        }
        BigInteger answer = BigInteger.ONE;
        for(int i = 1; i < num + 1; i++) {
            answer = answer.multiply(BigInteger.valueOf(i));
        }
        return answer;
    }
}
