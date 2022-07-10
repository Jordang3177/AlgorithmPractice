import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1360A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int tests = scan.nextInt();
        for(int i = 0; i < tests; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            if(a == 1 && b == 1) {
                System.out.println(4);
            }
            else if(a == 1) {
                System.out.println(b * b);
            }
            else if(b == 1) {
                System.out.println(a * a);
            }
            else if(a == b) {
                System.out.println((a * 2) * (b * 2));
            }
            else if(a > b) {
                if(b * 2 >= a) {
                    System.out.println((b * 2) * (b * 2));
                }
                else {
                    System.out.println(a * a);
                }
            }
            else {
                if(a * 2 >= b) {
                    System.out.println((a * 2) * (a * 2));
                }
                else {
                    System.out.println(b * b);
                }
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
