class Solution:
    def isPalindrome(self, s: str) -> bool:
        return True

    def testIsPalindrome(self):
        assert self.isPalindrome("A man, a plan, a canal: Panama") == True
        assert self.isPalindrome("race a car") == False
        assert self.isPalindrome("how about that") == False
        assert self.isPalindrome("a") == True
        assert self.isPalindrome("") == True
        assert self.isPalindrome("Aa") == True
        assert self.isPalindrome("ab") == False


if __name__ == "__main__":
    S = Solution()
    S.testIsPalindrome()
    print("All Tests Passed")