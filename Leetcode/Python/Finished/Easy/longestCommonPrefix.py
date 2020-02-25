class Solution:
    def longestCommonPrefix(self, strs):
        """
        given an array of strings, returns they longest common prefix
        :param strs: array of strings
        :return: str
        """
        if not strs:
            return ''
        first, last, i = min(strs), max(strs), 0
        answer = ''
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return answer
            answer += first[i]
            i += 1
        return answer

    def testLongestCommonPrefix(self):
        assert self.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
        assert self.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
        assert self.longestCommonPrefix(['wow', 'wellthenwow', 'wosswow']) == 'w'
        assert self.longestCommonPrefix(['wow', 'wow', 'wow', 'wow', 'wow']) == 'wow'
        assert self.longestCommonPrefix(['lol', 'lol', 'lol', 'lol', 'ololol', 'n']) == ''
        assert self.longestCommonPrefix(['okthen', 'lol', 'wow', 'only']) == ''
        assert self.longestCommonPrefix([]) == ''
        assert self.longestCommonPrefix(['one']) == 'one'


if __name__ == '__main__':
    S = Solution()
    S.testLongestCommonPrefix()
    print('All Tests Passed')
