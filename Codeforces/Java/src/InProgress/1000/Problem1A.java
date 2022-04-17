import java.util.Scanner;
public class Problem1A {
    public static void main(String[] args) {
        int n, m, a;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();
        a = input.nextInt();
        long answer = 0;
        answer += Math.ceil((double) n / a);
        answer *= Math.ceil((double) m / a);
        System.out.println(answer);
    }
}
