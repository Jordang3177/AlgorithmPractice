public class Problem005 {
    public static void main(String[] args) {
        Problem005 obj = new Problem005();
        long firstTest = obj.SmallestMultiple(10);
        System.out.println(firstTest);
        long secondTest = obj.SmallestMultiple(20);
        System.out.println(secondTest);
    }

    private long SmallestMultiple(int upperLimit) {
        int[] factors = new int[upperLimit];
        for(int i = 0; i < factors.length; i++) {
            factors[i] = i + 1;
        }
        for(long i = upperLimit; true; i += upperLimit) {
            boolean found = true;
            for (int factor : factors) {
                if (i % factor != 0) {
                    found = false;
                    break;
                }
            }
            if(found) {
                return i;
            }
        }
    }
}
