import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem151A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int friends = scan.nextInt();
        int bottles = scan.nextInt();
        int liters = scan.nextInt();
        int limes = scan.nextInt();
        int slices = scan.nextInt();
        int salt = scan.nextInt();
        int neededLiters = scan.nextInt();
        int neededSalt = scan.nextInt();
        int totalLiters = bottles * liters;
        int totalSlices = limes * slices;
        int totalSalt = salt / neededSalt;
        int totalDrinks = totalLiters / neededLiters;
        int min = Math.min(totalDrinks, Math.min(totalSlices, totalSalt));
        int answer = min / friends;
        System.out.println(answer);
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
