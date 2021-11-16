public class Problem006 {
    public static void main(String[] args) {
        Problem006 obj = new Problem006();
        long firstTest = obj.SumSquareDifference(10);
        System.out.println(firstTest);
        long secondTest = obj.SumSquareDifference(100);
        System.out.println(secondTest);
    }

    private long SumSquareDifference(int limit) {
        long sumOne = 0;
        long sumTwo = 0;
        for(int i = 1; i <= limit; i++) {
            sumOne += Math.pow(i, 2);
            sumTwo += i;
        }
        sumTwo = (long)Math.pow(sumTwo, 2);
        return sumTwo - sumOne;
    }
}
