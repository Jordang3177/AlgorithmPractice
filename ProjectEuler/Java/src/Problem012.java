public class Problem012 {
    public static void main(String[] args){
        Problem012 obj = new Problem012();
        long answer = obj.HighlyDivisibleTriangularNumber(500);
        System.out.println(answer);
    }

    private long HighlyDivisibleTriangularNumber(int divisorsLimit) {
        int divisors = 0;
        long answer = 0;
        int triangleNumber = 0;
        int i = 1;
        while(divisors < divisorsLimit) {
            triangleNumber += i;
            divisors = 0;
            i++;
            int end = (int)Math.pow(triangleNumber, 0.5);
            for(int j = 1; j < end; j++) {
                if(triangleNumber % j == 0) {
                    divisors++;
                }
            }
            divisors *= 2;
            if(end * end == triangleNumber) {
                divisors++;
            }
            answer = triangleNumber;
        }
        return answer;
    }
}
