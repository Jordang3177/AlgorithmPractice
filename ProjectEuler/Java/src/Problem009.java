public class Problem009 {
    public static void main(String[] args) {
        Problem009 obj = new Problem009();
        System.out.println(obj.SpecialPythagoreanTriplet());
    }

    private int SpecialPythagoreanTriplet() {
        int answer = 1;
        for(int i = 0; i < 1000; i++) {
            for(int j = i + 1; j < 1000; j++) {
                double cSquared = Math.pow(i, 2) + Math.pow(j, 2);
                double c = Math.pow(cSquared, 0.5);

                if(i + j + c == 1000) {
                    answer = (int) (i * j * c);
                }
            }
        }
        return answer;
    }
}
