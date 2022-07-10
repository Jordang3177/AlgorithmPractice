import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1353B {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int tests = scan.nextInt();
        for(int i = 0; i < tests; i++) {
            int size = scan.nextInt();
            int swaps = scan.nextInt();
            int[] a = new int[size];
            int[] b = new int[size];
            for(int j = 0; j < size; j++) {
                a[j] = scan.nextInt();
            }
            for(int j = 0; j < size; j++) {
                b[j] = scan.nextInt();
            }
            Arrays.sort(a);
            Arrays.sort(b);
            int aPointer = 0;
            int bPointer = size - 1;
            for(int j = 0; j < swaps; j++) {
                int aElement = a[aPointer];
                int bElement = b[bPointer];
                if(aElement >= bElement) {
                    break;
                }
                else {
                    a[aPointer] = bElement;
                    b[bPointer] = aElement;
                    aPointer++;
                    bPointer--;
                }
            }
            int answer = 0;
            for(int j = 0; j < size; j++) {
                answer += a[j];
            }
            System.out.println(answer);
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
