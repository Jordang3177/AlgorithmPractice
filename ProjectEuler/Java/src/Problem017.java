public class Problem017 {
    public static String[] ones =
            { "","one","two","three","four","five","six","seven","eight","nine","ten",
                    "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};

    public static String[] tens =
            {"","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"};

    public static String[] hundreds =
            {"","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred",
                    "sevenhundred","eighthundred","ninehundred"};

    public static void main(String[] args) {
        Problem017 obj = new Problem017();
        long firstTest = obj.NumberLetterCounts(5);
        System.out.println(firstTest);
        long secondTest = obj.NumberLetterCounts(1000);
        System.out.println(secondTest);
    }

    public long NumberLetterCounts(int limit) {
        long answer = 0;
        for(int i = 0; i <= limit; i++) {
            answer += WordLetterCount(i);
        }
        return answer;
    }

    public long WordLetterCount(int number) {
        if(number < 20) {
            return ones[number].length();
        }
        if(number < 100) {
            return tens[number/10].length() + ones[number % 10].length();
        }
        if(number == 1000) {
            return "onethousand".length();
        }
        if(number % 100 == 0) {
            return hundreds[number / 100].length();
        }
        if(number <= 999) {
            return hundreds[number / 100].length() + WordLetterCount(number % 100) + 3;
        }
        return 0;
    }
}
