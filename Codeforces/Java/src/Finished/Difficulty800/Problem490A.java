import java.util.*;
import java.io.*;
import java.lang.Math;

public class Problem490A {
    public static void main(String[] args) {
        Map<Integer, ArrayList<Integer>> olympiads = new HashMap<>();
        olympiads.put(1, new ArrayList<>());
        olympiads.put(2, new ArrayList<>());
        olympiads.put(3, new ArrayList<>());
        FastReader scan = new FastReader();
        int n = scan.nextInt();
        for(int i = 0; i < n; i++) {
            int olympiad = scan.nextInt();
            ArrayList<Integer> currentOlympiadList = olympiads.get(olympiad);
            currentOlympiadList.add(i + 1);
            olympiads.put(olympiad, currentOlympiadList);
        }
        ArrayList<Integer> programmingOlympiads = olympiads.get(1);
        ArrayList<Integer> mathOlympiads = olympiads.get(2);
        ArrayList<Integer> peOlympiads = olympiads.get(3);
        int answer = 0;
        ArrayList<ArrayList<Integer>> olympiadTeams = new ArrayList<>();
        while(!programmingOlympiads.isEmpty() && !mathOlympiads.isEmpty() && !peOlympiads.isEmpty()) {
            ArrayList<Integer> currentOlympiadTeam = new ArrayList<>();
            currentOlympiadTeam.add(programmingOlympiads.get(0));
            programmingOlympiads.remove(0);
            currentOlympiadTeam.add(mathOlympiads.get(0));
            mathOlympiads.remove(0);
            currentOlympiadTeam.add(peOlympiads.get(0));
            peOlympiads.remove(0);
            answer += 1;
            olympiadTeams.add(currentOlympiadTeam);
        }
        System.out.println(answer);
        for(int i = 0; i < answer; i++) {
            ArrayList<Integer> currentOlympiadTeam = olympiadTeams.get(i);
            System.out.println(String.valueOf(currentOlympiadTeam.get(0)) + " " + String.valueOf(currentOlympiadTeam.get(1)) + " " + String.valueOf(currentOlympiadTeam.get(2)));
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
