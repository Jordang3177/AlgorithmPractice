class Solution:
    def fib(self, N: int, memo = {0: 0, 1:1}) -> int:
        if N in memo:
            return memo[N]
        else:
            memo[N] = self.fib(N - 1) + self.fib(N - 2)
        return memo[N]

    def testFib(self):
        assert self.fib(0) == 0
        assert self.fib(1) == 1
        assert self.fib(2) == 1
        assert self.fib(3) == 2
        assert self.fib(4) == 3
        assert self.fib(5) == 5
        assert self.fib(6) == 8
        assert self.fib(7) == 13
        assert self.fib(8) == 21
        assert self.fib(9) == 34
        assert self.fib(10) == 55
        assert self.fib(20) == 6765
        assert self.fib(30) == 832040
        assert self.fib(40) == 102334155
        assert self.fib(50) == 12586269025
        assert self.fib(75) == 2111485077978050
        assert self.fib(100) == 354224848179261915075
        assert self.fib(150) == 9969216677189303386214405760200
        assert self.fib(200) == 280571172992510140037611932413038677189525
        assert self.fib(250) == 7896325826131730509282738943634332893686268675876375
        assert self.fib(300) == 222232244629420445529739893461909967206666939096499764990979600

if __name__ == '__main__':
    S = Solution()
    S.testFib()
    print("All Tests Passed")