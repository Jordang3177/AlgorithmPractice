public class Problem014 {
    public static void main(String[] args) {
        Problem014 obj = new Problem014();
        long firstTest = obj.LongestCollatzSequence(1000000);
        System.out.println(firstTest);
    }

    private long LongestCollatzSequence(long limit) {
        long answer = 0;
        long chain = 0;
        for(int i = 1; i < limit; i++) {
            long holder = i;
            long currentChain = 0;
            while(holder != 1) {
                if(holder % 2 == 0) {
                    holder /= 2;
                    currentChain++;
                }
                else {
                    holder = 3 * holder + 1;
                    currentChain++;
                }
            }
            if(currentChain > chain) {
                chain = currentChain;
                answer = i;
            }
        }
        return answer;
    }
}
