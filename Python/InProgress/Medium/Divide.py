class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        return 0

    def testDivide(self):
        assert self.divide(10, 3) == 3
        assert self.divide(7, -3) == -2


if __name__ == '__main__':
    S = Solution()
    S.testDivide()
    print("All Tests Passed")