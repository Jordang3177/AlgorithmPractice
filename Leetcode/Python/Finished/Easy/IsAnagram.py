class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words = {}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for value in alphabet:
            words[value] = 0
        for i in range(0, len(s)):
            words[s[i].lower()] += 1
            words[t[i].lower()] -= 1
        for value in words.values():
            if value != 0:
                return False
        return True
