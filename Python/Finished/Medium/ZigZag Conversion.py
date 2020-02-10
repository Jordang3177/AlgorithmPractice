class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        answer = [''] * (2*numRows - 2)
        row, step = 0, 0
        for value in s:
            answer[row] += value
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(answer)



    def testConvert(self):
        assert self.convert('PAYPALISHIRING', 3) == "PAHNAPLSIIGYIR"
        assert self.convert('PAYPALISHIRING', 4) == "PINALSIGYAHRPI"
        assert self.convert("He", 2) == 'He'
        assert self.convert('Hellotherepeople', 1) == 'Hellotherepeople'

if __name__ == '__main__':
    S = Solution()
    S.testConvert()
    print("All Tests Passed")