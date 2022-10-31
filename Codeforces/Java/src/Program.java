import java.util.*;

class Program {

    public int nonConstructibleChange(int[] coins) {
        if(coins.length == 0) {
            return 1;
        }
        Arrays.sort(coins);
        Set<Integer> coinsFound = new HashSet<>();
        for(int i = 0; i < coins.length; i++) {
            int currentCoin = coins[i];
            if (!coinsFound.contains(currentCoin)) {
                coinsFound.add(currentCoin);
                if (coinsFound.size() != currentCoin) {
                    return coinsFound.size();
                }
            }
            for (int j = 0; j < i; j++) {
                int lastCoin = coins[j];
                int nextValue = currentCoin + lastCoin;
                if (!coinsFound.contains(nextValue)) {
                    coinsFound.add(nextValue);
                    if (coinsFound.size() != nextValue) {
                        return coinsFound.size();
                    }
                }
            }
        }
        return coinsFound.size() + 1;
    }

    public static void main(String[] args) {
        Program program = new Program();
        int[] coins = new int[] {5, 7, 1, 1, 2, 3, 22};
        int returnValue = program.nonConstructibleChange(coins);
        if(returnValue == 20) {
            System.out.println("Yay");
        }
        else {
            System.out.println(returnValue);
        }
    }
}