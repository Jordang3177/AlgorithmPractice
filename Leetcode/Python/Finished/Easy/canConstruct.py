class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        returns if the given magazine can be used to from the ransomNote
        :param ransomNote: String
        :param magazine: String
        :return: boolean
        """
        count_chars = {}
        for i in range(len(magazine)):
            if magazine[i] in count_chars:
                count_chars[magazine[i]] += 1
            else:
                count_chars[magazine[i]] = 1
        for char in ransomNote:
            if char in count_chars and count_chars[char] != 0:
                count_chars[char] -= 1
            else:
                return False
        return True