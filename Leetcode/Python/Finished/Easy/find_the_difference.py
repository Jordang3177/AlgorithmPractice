class Solution:
    def findTheDifference(self, s, t):
        """
        returns the character that is in t but not in s
        :param s: string
        :param t: string
        :return: string
        """
        chars_in_s = {}
        for char in s:
            if char in chars_in_s:
                chars_in_s[char] += 1
            else:
                chars_in_s[char] = 1
        for char in t:
            if char in chars_in_s:
                chars_in_s[char] -= 1
            else:
                return char
        for key, value in chars_in_s.items():
            if value == -1:
                return key