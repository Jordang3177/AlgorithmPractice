class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return 'yes'

    def testConvert(self):
        assert self.convert('PAYPALISHIRING', 3) == "PAHNAPLSIIGYIR"
        assert self.convert('PAYPALISHIRING', 4) == "PINALSIGYAHRPI"

if __name__ == '__main__':
    S = Solution()
    S.testConvert()
    print("All Tests Passed")