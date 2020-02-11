class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        if divisor > 0 and dividend > 0:
            while dividend >= divisor:
                dividend = dividend - divisor
                answer += 1
        if divisor < 0 and dividend > 0:
            while dividend >= abs(divisor):
                dividend = dividend + divisor
                answer -= 1
        if divisor < 0 and dividend < 0:
            while abs(dividend) >= abs(divisor):
                dividend = dividend - divisor
                answer += 1
        if divisor > 0 and dividend < 0:
            while abs(dividend) >= divisor:
                dividend = dividend + divisor
                answer -= 1
        if answer > 2**31 - 1:
            return 2**31 - 1
        if answer < -2**31:
            return -2**31
        else:
            return answer

    def testDivide(self):
        assert self.divide(10, 3) == 3
        assert self.divide(7, -3) == -2
        assert self.divide(-4, 2) == -2
        assert self.divide(-4, -2) == 2


if __name__ == '__main__':
    S = Solution()
    S.testDivide()
    print("All Tests Passed")