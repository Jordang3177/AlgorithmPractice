class Solution:
    def longestCommonPrefix(self, strs):
        """
        returns the longest common prefix among the given list of strings
        :param strs: List of String
        :return: String
        """
        if len(strs) < 1:
            return ''
        if len(strs) < 2:
            return strs[0]
        first, last, answer = min(strs), max(strs), []
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                answer.append(first[i])
            else:
                return ''.join(answer)
        return ''.join(answer)

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
