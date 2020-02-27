class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        phone = {'1': [''],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        lets = ['']
        for digit in digits:
            letL = []
            for value in lets:
                for alpha in phone[digit]:
                    letL.append(value + alpha)
            lets = letL
        return lets

    def testLetterCombinations(self):
        assert self.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


if __name__ == '__main__':
    S = Solution()
    S.testLetterCombinations()
    print("All Tests Passed")
