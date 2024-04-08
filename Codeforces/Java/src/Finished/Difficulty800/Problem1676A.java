package Finished.Difficulty800;

import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1676A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int tests = scan.nextInt();
        for(int i = 0; i < tests; i++) {
            String test = scan.nextLine();
            int firstHalf = 0;
            int secondHalf = 0;
            for(int j = 0; j < 3; j++) {
                int current = (int)test.charAt(j);
                firstHalf += current;
            }
            for(int j = 3; j < test.length(); j++) {
                int current = (int)test.charAt(j);
                secondHalf += current;
            }
            if(firstHalf == secondHalf) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
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
