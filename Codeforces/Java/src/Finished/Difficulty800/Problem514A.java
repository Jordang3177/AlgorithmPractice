import java.util.Scanner;

public class Problem514A {
    public static void main(String[] args) {
        int n, m;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();
        boolean lastLeft = false;
        for(int i = 0; i < n; i++) {
            StringBuilder currentLine = new StringBuilder();
            for(int j = 0; j < m; j++) {
                if(i % 2 == 0) {
                    currentLine.append('#');
                }
                else if(lastLeft) {
                    if(j == 0) {
                        currentLine.append('#');
                    }
                    else {
                        currentLine.append('.');
                    }
                }
                else {
                    if(j == m - 1) {
                        currentLine.append('#');
                    }
                    else {
                        currentLine.append('.');
                    }
                }
            }
            if(i % 2 != 0) {
                lastLeft = !lastLeft;
            }
            System.out.println(currentLine.toString());
        }
    }
}
