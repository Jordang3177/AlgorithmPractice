import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem977B {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int size = scan.nextInt();
        Map<String, Integer> grams = new HashMap<>();
        String gram = scan.nextLine();
        String twoGram = new String();
        int mostOccurrences = 0;
        for(int i = 0; i  < size - 1; i++) {
            StringBuilder gramBuilder = new StringBuilder();
            gramBuilder.append(gram.charAt(i));
            gramBuilder.append(gram.charAt(i + 1));
            String currentGram = gramBuilder.toString();
            if(grams.containsKey(currentGram)) {
                grams.put(currentGram, grams.get(currentGram) + 1);
                if(grams.get(currentGram) > mostOccurrences) {
                    twoGram = currentGram;
                    mostOccurrences = grams.get(currentGram);
                }
            }
            else {
                grams.put(currentGram, 1);
                twoGram = mostOccurrences == 0 ? currentGram : twoGram;
            }
        }
        System.out.println(twoGram);
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
