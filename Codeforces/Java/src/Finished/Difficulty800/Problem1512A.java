import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1512A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int tests = scan.nextInt();
        for(int i = 0; i < tests; i++) {
            int n = scan.nextInt();
            int firstNum = 0;
            int firstNumCount = 0;
            int firstNumIndex = 0;
            int secondNum = 0;
            int secondNumCount = 0;
            int secondNumIndex = 0;
            for(int j = 0; j < n; j++) {
                int nextNum = scan.nextInt();
                if(firstNum == 0) {
                    firstNum = nextNum;
                    firstNumCount++;
                    firstNumIndex = j + 1;
                }
                else if(firstNum != 0 && nextNum == firstNum) {
                    firstNumCount++;
                }
                else {
                    secondNum = nextNum;
                    secondNumCount++;
                    secondNumIndex = j + 1;
                }
            }
            if(firstNumCount == 1) {
                System.out.println(firstNumIndex);
            }
            else {
                System.out.println(secondNumIndex);
            }
        }
    }
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
  
        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
        }
  
        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
  
        int nextInt() { return Integer.parseInt(next()); }
  
        long nextLong() { return Long.parseLong(next()); }
  
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
  
        String nextLine()
        {
            String str = "";
            try {
                if(st.hasMoreTokens()){
                    str = st.nextToken("\n");
                }
                else{
                    str = br.readLine();
                }
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
