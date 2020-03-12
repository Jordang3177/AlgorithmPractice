package Finished.Easy;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class FizzBuzz_412 {
    public static void main(String[] args){
        System.out.println(new FizzBuzz_412().fizzBuzz(1));
        System.out.println(new FizzBuzz_412().fizzBuzz(15));
    }

    /**
     * Takes a number and returns a list of strings with the index being the appropriate String based on the FizzBuzz Game.
     * @param n The number of elements to be in the Array
     * @return Array of Strings
     **/
    public List<String> fizzBuzz(int n) {

        List<String> ans = new ArrayList<String>();

        for (int i = 1; i <= n; i++) {
            boolean divisibleBy3 = (i % 3 == 0);
            boolean divisibleBy5 = (i % 5 == 0);

            if (divisibleBy3 && divisibleBy5) {
                ans.add("FizzBuzz");
            }
            else if (divisibleBy3) {
                ans.add("Fizz");
            }
            else if (divisibleBy5) {
                ans.add("Buzz");
            }
            else {
                ans.add(Integer.toString(i));
            }
        }

        return ans;
    }

    @Test
    public void TestFizzBuzz() {
        Assert.assertEquals(["1"], fizzBuzz(1));
    }
}
