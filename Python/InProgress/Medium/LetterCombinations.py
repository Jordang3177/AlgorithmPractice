class Solution:
    def letterCombinations(self, digits):
        twos = ['a', 'b', 'c']
        threes = ['d', 'e', 'f']
        fours = ['g', 'h', 'i']
        fives = ['j', 'k', 'l']
        sixes = ['m', 'n', 'o']
        sevens = ['p', 'q', 'r', 's']
        eights = ['t', 'u', 'v']
        nines = ['w', 'x', 'y', 'z']
        combos = {2: twos, 3: threes, 4: fours, 5: fives, 6: sixes, 7: sevens, 8: eights, 9: nines}
        answer = []
        holder = []

    def testLetterCombinations(self):
        assert self.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


if __name__ == '__main__':
    S = Solution()
    S.testLetterCombinations()
    print("All Tests Passed")
