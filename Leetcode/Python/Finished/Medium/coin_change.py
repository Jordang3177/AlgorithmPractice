class Solution:
    def coinChange(self, coins, amount):
        """
        returns the minimum amount of coins that can be given from coins to be equal to amount
        :param coins: Array of int
        :param amount: int
        :return: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    break
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
