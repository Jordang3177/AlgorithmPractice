import java.util.ArrayList;
import java.util.Scanner;

public class Problem1352A {
    public static void main(String[] args) {
        int t;
        Scanner input = new Scanner(System.in);
        t = input.nextInt();
        for(int i = 0; i < t; i++){
            int n;
            n = input.nextInt();
            int place = 1;
            ArrayList<Integer> currentNumbers = new ArrayList<>();
            while(n >= 1) {
                if(n % 10 != 0) {
                    int nextInt = n % 10;
                    nextInt *= place;
                    currentNumbers.add(nextInt);
                }
                n /= 10;
                place *= 10;
            }
            System.out.println(currentNumbers.size());
            for(int j = 0; j < currentNumbers.size(); j++) {
                if(j != currentNumbers.size() - 1) {
                    System.out.print(currentNumbers.get(j));
                    System.out.print(" ");
                }
                else {
                    System.out.println(currentNumbers.get(j));
                }
            }
        }
    }
}
