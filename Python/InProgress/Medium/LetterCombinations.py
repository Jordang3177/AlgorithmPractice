class Solution:
    def letterCombinations(self, digits):
        return 'ab'

    def testLetterCombinations(self):
        assert self.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

if __name__ == '__main__':
    S = Solution()
    S.testLetterCombinations()
    print("All Tests Passed")
