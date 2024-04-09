package Finished.Difficulty800;

import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem9A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int a = scan.nextInt();
        int b = scan.nextInt();
        if(a < b) {
            int up = 6 - b + 1;
            if(up == 1) {
                System.out.println("1/6");
            }
            if(up == 2) {
                System.out.println("1/3");
            }
            if(up == 3) {
                System.out.println("1/2");
            }
            if(up == 4) {
                System.out.println("2/3");
            }
            if(up == 5) {
                System.out.println("5/6");
            }
            if(up == 6) {
                System.out.println("1/1");
            }
        }
        else {
            int up = 6 - a + 1;
            if(up == 1) {
                System.out.println("1/6");
            }
            if(up == 2) {
                System.out.println("1/3");
            }
            if(up == 3) {
                System.out.println("1/2");
            }
            if(up == 4) {
                System.out.println("2/3");
            }
            if(up == 5) {
                System.out.println("5/6");
            }
            if(up == 6) {
                System.out.println("1/1");
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
