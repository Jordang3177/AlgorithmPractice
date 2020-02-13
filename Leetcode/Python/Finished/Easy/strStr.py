class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

    def teststrStr(self):
        assert self.strStr('hello', 'll') == 2
        assert self.strStr("aaaaaaa", 'bba') == -1
        assert self.strStr('wow', 'ow') == 1
        assert self.strStr('What about this string', 'at') == 2
        assert self.strStr('When When', 'he') == 1
        assert self.strStr('Wow', 'wowoww') == -1
        assert self.strStr('Same', 'Same') == 0
        assert self.strStr('wow', '') == 0
        assert self.strStr('mississippi', 'issipi') == -1
        assert self.strStr('mississippi', 'issip') == 4

if __name__ == '__main__':
    S = Solution()
    S.teststrStr()
    print('All Tests Passed')