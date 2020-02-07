class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        while num != 0:
            if num >= 1000:
                answer += 'M'
                num -= 1000
                continue
            if num >= 900:
                answer += 'CM'
                num -= 900
                continue
            if num >= 500:
                answer += 'D'
                num -= 500
                continue
            if num >= 400:
                answer += 'CD'
                num -= 400
                continue
            if num >= 100:
                answer += 'C'
                num -= 100
                continue
            if num >= 90:
                answer += 'XC'
                num -= 90
                continue
            if num >= 50:
                answer += 'L'
                num -= 50
                continue
            if num >= 40:
                answer += 'XL'
                num -= 40
                continue
            if num >= 10:
                answer += 'X'
                num -= 10
                continue
            if num >= 9:
                answer += 'IX'
                num -= 9
                continue
            if num >= 5:
                answer += 'V'
                num -= 5
                continue
            if num >= 4:
                answer += 'IV'
                num -= 4
                continue
            if num >= 1:
                answer += 'I'
                num -= 1
                continue
        return answer


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