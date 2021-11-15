public class Problem001 {
    public static void main(String[] args) {
        System.out.println(MultiplesOf3And5(1000));
    }

    public static int MultiplesOf3And5(int limit) {
        int sum = 0;
        for(int i = 3; i < limit; i += 3) {
            sum += i;
        }
        for(int i = 5; i < limit; i += 5) {
            sum += i;
        }
        for(int i = 15; i < limit; i += 15) {
            sum -= i;
        }
        return sum;
    }
}
