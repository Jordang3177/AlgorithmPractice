import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1367B {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int tests = scan.nextInt();
        for(int i = 0; i < tests; i++) {
            int size = scan.nextInt();
            int[] a = new int[size];
            int evens = 0;
            int odds = 0;
            for(int j = 0; j < size; j++) {
                int b = scan.nextInt();
                if(j % 2 == b % 2) {
                    continue;
                }
                else if(b % 2 == 0){
                    evens++;
                }
                else {
                    odds++;
                }
            }
            if(evens != odds) {
                System.out.println(-1);
            }
            else {
                System.out.println(evens);
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
