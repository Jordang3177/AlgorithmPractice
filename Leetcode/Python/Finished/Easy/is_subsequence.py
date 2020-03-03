class Solution:
    def isSubsequence(self, s, t):
        """
        determines if s is a subsequence of t
        :param s: string
        :param t: string
        :return: boolean
        """
        if s == '':
            return True
        index = 0
        for i in range(len(t)):
            if s[index] == t[i]:
                index += 1
            if index == len(s):
                break
        if index == len(s):
            return True
        return False
