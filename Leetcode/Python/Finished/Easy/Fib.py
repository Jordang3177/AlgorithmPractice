class Solution:
    def fib(self, N: int, memo = {0: 0, 1:1}) -> int:
        """
        Function to return the fibonacci number of N
        :param N: int
        :param memo: dict
        :return: int
        """
        if N in memo:
            return memo[N]
        else:
            memo[N] = self.fib(N - 1) + self.fib(N - 2)
        return memo[N]
