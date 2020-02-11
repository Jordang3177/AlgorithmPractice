class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        i = 0
        j = len(s) - 1
        while i != j:
            if i > j:
                break
            if s[i].isalpha() == False and s[i].isnumeric() == False:
                i += 1
                continue
            if s[j].isalpha() == False and s[j].isnumeric() == False:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


    def testIsPalindrome(self):
        assert self.isPalindrome("A man, a plan, a canal: Panama") == True
        assert self.isPalindrome("race a car") == False
        assert self.isPalindrome("how about that") == False
        assert self.isPalindrome("a") == True
        assert self.isPalindrome("") == True
        assert self.isPalindrome("Aa") == True
        assert self.isPalindrome("ab") == False
        assert self.isPalindrome('0P') == False


if __name__ == "__main__":
    S = Solution()
    S.testIsPalindrome()
    print("All Tests Passed")