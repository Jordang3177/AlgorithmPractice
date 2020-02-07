class Solution:
    def trailingZeroes(self, n: int):
        if n < 5:
            return 0
        else:
            answer = 0
            while n != 0:
                n //= 5
                answer += n
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
        assert self.trailingZeroes(22) == 4
        assert self.trailingZeroes(23) == 4
        assert self.trailingZeroes(24) == 4
        assert self.trailingZeroes(25) == 6
        assert self.trailingZeroes(30) == 7
        assert self.trailingZeroes(35) == 8
        assert self.trailingZeroes(50) == 12
        assert self.trailingZeroes(100) == 24
        assert self.trailingZeroes(500) == 124
        assert self.trailingZeroes(5000) == 1249
        assert self.trailingZeroes(1000000) == 249998


if __name__ == "__main__":
    S = Solution()
    S.testTrailingZeroes()
    print("All Tests Passed")