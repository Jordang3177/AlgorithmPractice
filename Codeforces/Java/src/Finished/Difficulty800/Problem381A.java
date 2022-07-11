import java.io.*;
import java.util.*;
import java.lang.*;

public class Problem381A {
    public static void main(String[] args) {
        FastReader scan = new FastReader();
        int size = scan.nextInt();
        ArrayList<Integer> cards = new ArrayList<>();
        for(int i = 0; i < size; i++) {
            cards.add(scan.nextInt());
        }
        int a = 0;
        int b = 0;
        boolean turn = true;
        while(!cards.isEmpty()) {
            int left = cards.get(0);
            int right = cards.get(cards.size() - 1);
            if(left > right) {
                if(turn) {
                    a += left;
                    turn = !turn;
                    cards.remove(0);
                }
                else {
                    b += left;
                    turn = !turn;
                    cards.remove(0);
                }
            }
            else {
                if(turn) {
                    a += right;
                    turn = !turn;
                    cards.remove(cards.size() - 1);
                }
                else {
                    b += right;
                    turn = !turn;
                    cards.remove(cards.size() - 1);
                }
            }
        }
        System.out.println(String.valueOf(a) + " " + String.valueOf(b));
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
