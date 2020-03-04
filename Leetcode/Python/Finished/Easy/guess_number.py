# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        a function to guess what the hidden number is
        :param n: int
        :return: int
        """
        low = 1
        high = n
        while low <= high:
            mid = int(low + (high - low) / 2)
            result = guess(mid)
            if result == 0:
                return mid
            elif result < 0:
                high = mid - 1
            else:
                low = mid + 1

