class Solution:
    memo = {0: 1, 1: 1}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]

    def test(self):
        assert self.climbStairs(0) == 1
        assert self.climbStairs(1) == 1
        assert self.climbStairs(2) == 2
        assert self.climbStairs(3) == 3
        assert self.climbStairs(4) == 5
        assert self.climbStairs(5) == 8
        assert self.climbStairs(6) == 13
        assert self.climbStairs(7) == 21
        assert self.climbStairs(8) == 34
        assert self.climbStairs(9) == 55
        assert self.climbStairs(10) == 89

if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")