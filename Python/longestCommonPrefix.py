class Solution:
    def longestCommonPrefix(self, strs):
        print('work in Progrees')

    def testLongestCommonPrefix(self):
        assert self.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
        assert self.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
        assert self.longestCommonPrefix(['wow', 'wellthenwow', 'wosswow']) == 'wow'
        assert self.longestCommonPrefix(['wow', 'wow', 'wow', 'wow', 'wow']) == 'wow'
        assert self.longestCommonPrefix(['lol', 'lol', 'lol', 'lol', 'ololol', 'n']) == ''
        assert self.longestCommonPrefix(['okthen', 'lol', 'wow', 'only']) == 'o'

if __name__ == '__main__':
    S = Solution()
    S.testLongestCommonPrefix()
    print('All Tests Passed')
