class Solution:
    def trailingZeroes(self, n: int):
        return n

    def testTrailingZeroes(self):
        assert self.trailingZeroes(3) == 0
        assert self.trailingZeroes(5) == 1
        assert self.trailingZeroes(0) == 0
        assert self.trailingZeroes(1) == 0
        assert self.trailingZeroes(2) == 0
        assert self.trailingZeroes(4) == 0
        assert self.trailingZeroes(6) == 1
        assert self.trailingZeroes(7) == 1
        assert self.trailingZeroes(8) == 1
        assert self.trailingZeroes(9) == 1
        assert self.trailingZeroes(10) == 3
        assert self.trailingZeroes(11) == 2
        assert self.trailingZeroes(12) == 2
        assert self.trailingZeroes(13) == 2
        assert self.trailingZeroes(14) == 2
        assert self.trailingZeroes(15) == 3
        assert self.trailingZeroes(16) == 3
        assert self.trailingZeroes(17) == 3
        assert self.trailingZeroes(18) == 3
        assert self.trailingZeroes(19) == 3

if __name__ == "__main__":
    S = Solution()
    S.testTrailingZeroes()
    print("All Tests Passed")