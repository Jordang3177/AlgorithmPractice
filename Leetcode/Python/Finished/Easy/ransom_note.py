class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for char in ransomNote:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in magazine:
            if char in count:
                count[char] -= 1
        for key, value in count.items():
            if value > 0:
                return False
        return True
