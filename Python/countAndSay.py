class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        holder = 2
        answer = '1'
        return 'work in progress'

    def testCountAndSay(self):
        assert self.countAndSay(1) == '1'
        assert self.countAndSay(4) == '1211'
        assert self.countAndSay(2) == '11'
        assert self.countAndSay(3) == '21'
        assert self.countAndSay(5) == '111221'
        assert self.countAndSay(6) == '312211'
        assert self.countAndsay(7) == '13112221'
        assert self.countAndSay(8) == '1113213211'
        assert self.countAndSay(9) == '31131211131221'
        assert self.countAndSay(10) == '13211311123113112211'

if __name__ == '__main__':
    S = Solution()
    S.testCountAndSay()
    print("All Tests Passed")