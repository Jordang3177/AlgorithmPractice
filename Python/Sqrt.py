class Solution:
    def mySqrt(self, x: int) -> int:
        return 0

    def testMySqrt(self):
        assert self.mySqrt(2) == 1
        assert self.mySqrt(3) == 1
        assert self.mySqrt(4) == 2
        assert self.mySqrt(5) == 2
        assert self.mySqrt(6) == 2
        assert self.mySqrt(7) == 2
        assert self.mySqrt(8) == 2
        assert self.mySqrt(9) == 3
        assert self.mySqrt(10) == 3
        assert self.mySqrt(11) == 3
        assert self.mySqrt(12) == 3
        assert self.mySqrt(13) == 3
        assert self.mySqrt(14) == 3
        assert self.mySqrt(15) == 3
        assert self.mySqrt(16) == 4

if __name__ == '__main__':
    S = Solution()
    S.testMySqrt()
    print('All Tests Passed')
