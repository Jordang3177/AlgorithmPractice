class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        find the first unique character in a string and return it's index
        :param s: string
        :return: int
        """
        char_count = {}
        for i in range(len(s)):
            if s[i] in char_count:
                char_count[s[i]][0] += 1
            else:
                char_count[s[i]] = [1,i]
        for values in char_count.values():
            if values[0] == 1:
                return values[1]
        return -1