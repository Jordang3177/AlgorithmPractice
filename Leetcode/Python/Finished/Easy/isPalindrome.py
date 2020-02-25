class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        given an int, returns if it's a palindrome
        :param x: x
        :return: bool
        """
        y = str(x)
        if len(y) == 0:
            return True
        if len(y) == 1:
            return True
        if len(y) == 2:
            return y[0] == y[1]
        if y[0] == '-':
            return False
        if len(y) % 2:
            first_half = y[0:int(len(y)/2)]
            second_half = y[int(len(y)/2):len(y)]
            i = 0
            for num in first_half:
                if num != second_half[len(second_half) - 1 - i]:
                    return False
                i += 1
            return True
        else:
            first_half = y[0:int(len(y)/2)]
            second_half = y[int(len(y)/2) + 1: len(y)]
            i = 0
            for num in first_half:
                if num != second_half[len(second_half) - 1 - i]:
                    return False
                i += 1
            return True

    def test_isPalindrome(self):
        assert self.isPalindrome(121) == True
        assert self.isPalindrome(-121) == False
        assert self.isPalindrome(122) == False
        assert self.isPalindrome(1) == True
        assert self.isPalindrome(0) == True
        assert self.isPalindrome(111111111) == True
        assert self.isPalindrome(1010101010101) == True
        assert self.isPalindrome(10) == False

if __name__ == "__main__":
    S = Solution()
    S.test_isPalindrome()
    print("All Tests Passed")