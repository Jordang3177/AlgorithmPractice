class Solution:
    def intToRoman(self, num: int) -> str:
        return 'I'

    def testIntToRoman(self):
        assert self.intToRoman(1) == 'I'
        assert self.intToRoman(2) == 'II'
        assert self.intToRoman(4) == 'IV'
        assert self.intToRoman(5) == 'V'
        assert self.intToRoman(9) == 'IX'
        assert self.intToRoman(10) == 'X'
        assert self.intToRoman(14) == 'XIV'
        assert self.intToRoman(40) == 'XL'
        assert self.intToRoman(50) == 'L'
        assert self.intToRoman(90) == 'XC'
        assert self.intToRoman(100) == 'C'
        assert self.intToRoman(500) == 'D'
        assert self.intToRoman(1000) == 'M'
        assert self.intToRoman(400) == 'CD'
        assert self.intToRoman(900) == 'CM'
        assert self.intToRoman(58) == 'LVIII'
        assert self.intToRoman(1994) == 'MCMXCIV'

if __name__ == '__main__':
    S = Solution()
    S.testIntToRoman()
    print("All Tests Passed")