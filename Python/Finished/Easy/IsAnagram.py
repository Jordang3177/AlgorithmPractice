class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words = {}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for value in alphabet:
            words[value] = 0
        for i in range(0, len(s)):
            words[s[i]] += 1
            words[t[i]] -= 1
        for value in words.values():
            if value != 0:
                return False
        return True


    def testIsAnagram(self):
        assert self.isAnagram('anagram', 'nagaram') == True
        assert self.isAnagram('rat', 'car') == False
        assert self.isAnagram('too', 'oto') == True
        assert self.isAnagram('howaboutnow', 'howaboutnoo') == False

if __name__ == '__main__':
    S = Solution()
    S.testIsAnagram()
    print("All Tests Passed")