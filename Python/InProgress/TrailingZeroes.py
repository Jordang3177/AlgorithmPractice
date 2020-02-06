import math

class Solution:
    def trailingZeroes(self, n: int):
        if n < 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 0
        else:
            fact = math.factorial(n)
            answer = 0
            i = len(str(fact)) - 1
            sfact = str(fact)
            while i >= 0:
                if sfact[i] == '0':
                    answer += 1
                    i = i - 1
                else:
                    return answer

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
        assert self.trailingZeroes(10) == 2
        assert self.trailingZeroes(11) == 2
        assert self.trailingZeroes(12) == 2
        assert self.trailingZeroes(13) == 2
        assert self.trailingZeroes(14) == 2
        assert self.trailingZeroes(15) == 3
        assert self.trailingZeroes(16) == 3
        assert self.trailingZeroes(17) == 3
        assert self.trailingZeroes(18) == 3
        assert self.trailingZeroes(19) == 3
        assert self.trailingZeroes(20) == 4
        assert self.trailingZeroes(21) == 4

if __name__ == "__main__":
    S = Solution()
    S.testTrailingZeroes()
    print("All Tests Passed")