class Solution:
    def strStr(self, haystack: str, needle: str):
        if len(needle) > len(haystack):
            return -1
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
        if len(needle) == 0:
            return 0
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                answer = i
                if len(needle) == 1:
                    return answer
                if len(haystack[i:]) < len(needle):
                    return -1
                if needle in haystack[i:len(needle) + i]:
                    return answer
        return -1





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