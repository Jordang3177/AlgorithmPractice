import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem1520A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int t = scan.nextInt();
        for(int i = 0; i < t; i++) {
            Set<Character> seenTasks = new HashSet<>();
            int size = scan.nextInt();
            String tasks = scan.nextLine();
            char previousChar = tasks.charAt(0);
            seenTasks.add(previousChar);
            boolean seen = false;
            for(int j = 1; j < tasks.length(); j++) {
                char currentChar = tasks.charAt(j);
                if(currentChar == previousChar) {
                    continue;
                }
                else if(seenTasks.contains(currentChar)){
                    seen = true;
                    break;
                }
                else {
                    previousChar = currentChar;
                    seenTasks.add(currentChar);
                }
            }
            String result = seen ? "NO" : "YES";
            System.out.println(result);
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
