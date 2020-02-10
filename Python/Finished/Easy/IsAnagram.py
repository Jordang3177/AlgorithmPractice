class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

    def testIsAnagram(self):
        assert self.isAnagram('anagram', 'nagaram') == True
        assert self.isAnagram('rat', 'car') == False
        assert self.isAnagram('too', 'oto') == True
        assert self.isAnagram('howaboutnow', 'howaboutnoo') == False

if __name__ == '__main__':
    S = Solution()
    S.testIsAnagram()
    print("All Tests Passed")