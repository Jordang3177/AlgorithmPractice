import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1433A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int test = scan.nextInt();
        for(int i = 0; i < test; i++) {
            int apartment = scan.nextInt();
            int sum = 0;
            int digit = apartment % 10;
            sum += (digit - 1) * 10;
            if(apartment < 10) {
                sum += 1;
            }
            else if(apartment < 100) {
                sum += 3;
            }
            else if(apartment < 1000) {
                sum += 6;
            }
            else {
                sum += 10;
            }
            System.out.println(sum);
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
