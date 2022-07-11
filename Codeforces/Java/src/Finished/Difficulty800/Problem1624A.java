import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1624A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int t = scan.nextInt();
        for(int i = 0; i < t; i++) {
            int size = scan.nextInt();
            int smallest = Integer.MAX_VALUE;
            int biggest = Integer.MIN_VALUE;
            for(int j = 0; j < size; j++) {
                int current = scan.nextInt();
                if(current < smallest) {
                    smallest = current;
                }
                if(current > biggest) {
                    biggest = current;
                }
            }
            System.out.println(biggest - smallest);
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
