class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if ' ' not in s:
            return len(s)
        if len(s) == 1 and s[0] == ' ':
            return 0
        while s[len(s) - 1] == ' ':
            s = s[0:len(s) - 1]
            if len(s) == 0:
                return 0
        if len(s) == 1:
            return len(s)
        if ' ' not in s:
            return len(s)
        i = len(s) - 1
        while i != -1:
            if s[i] == ' ':
                return len(s) - i - 1
            i = i - 1

    def testLenfthOfLastWord(self):
        assert self.lengthOfLastWord('wow') == 3
        assert self.lengthOfLastWord('Hello World') == 5
        assert self.lengthOfLastWord('') == 0
        assert self.lengthOfLastWord("well this is a predicament to be in isn't it, now and forever then") == 4
        assert self.lengthOfLastWord("now") == 3
        assert self.lengthOfLastWord('Ok then keep it going then why don\'t you') == 3
        assert self.lengthOfLastWord("Not sure what else for a base case or other tests is possible here") == 4
        assert self.lengthOfLastWord(" ") == 0
        assert self.lengthOfLastWord(" a") == 1
        assert self.lengthOfLastWord("a ") == 1
        assert self.lengthOfLastWord("      ") == 0
        assert self.lengthOfLastWord("a          ") == 1
        assert self.lengthOfLastWord("day       ") == 3
        assert self.lengthOfLastWord("Hello World how are you            ") == 3


if __name__ == '__main__':
    S = Solution()
    S.testLenfthOfLastWord()
    print("All Tests Passed")