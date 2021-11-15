public class Problem004 {
    public static void main(String[] args) {
        Problem004 obj = new Problem004();
        long twoDigitAnswer = obj.LargestPalindrome(2);
        System.out.println(twoDigitAnswer);
        long threeDigitAnswer = obj.LargestPalindrome(3);
        System.out.println(threeDigitAnswer);
    }

    private long LargestPalindrome(int digits){
        long largestPalindrome = 0;
        long startingNumber = (long) (Math.pow(10, digits) - 1);
        long endingNumber = (long) (Math.pow(10, digits - 1));
        for(long i = startingNumber; i >= endingNumber; i--) {
            for(long j = i; j >= endingNumber; j--) {
                long num = i * j;
                if(this.isPalindrome(num) && largestPalindrome < num) {
                    largestPalindrome = num;
                }
            }
        }
        return largestPalindrome;
    }

    private boolean isPalindrome(long num) {
        long checker = 0;
        long holder = num;
        while(holder != 0) {
            int currentPosition = (int)holder % 10;
            checker *= 10;
            checker += currentPosition;
            holder /= 10;
        }
        return checker == num;
    }
}
