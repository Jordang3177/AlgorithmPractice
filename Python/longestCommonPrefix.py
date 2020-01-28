class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        counter = 0
        answer = ''
        previous = False
        for char in strs[0]:
            for str in strs:
                if char in str:
                    counter += 1
                else:
                    print('work in progress')

    def testLongestCommonPrefix(self):
        assert self.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
        assert self.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
        assert self.longestCommonPrefix(['wow', 'wellthenwow', 'wosswow']) == 'wow'
        assert self.longestCommonPrefix(['wow', 'wow', 'wow', 'wow', 'wow']) == 'wow'
        assert self.longestCommonPrefix(['lol', 'lol', 'lol', 'lol', 'ololol', 'n']) == ''
        assert self.longestCommonPrefix(['okthen', 'lol', 'wow', 'only']) == 'o'
        assert self.longestCommonPrefix([]) == ''
        assert self.longestCommonPrefix(['one']) == 'one'


if __name__ == '__main__':
    S = Solution()
    S.testLongestCommonPrefix()
    print('All Tests Passed')
