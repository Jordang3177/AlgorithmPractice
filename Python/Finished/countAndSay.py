class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        holder = 1
        answer = ''
        num = 0
        previous = '1'
        previousAnswer = '1'
        while holder != n:
            for i in range(0, len(previousAnswer)):
                if previousAnswer[i] != previous:
                    answer += str(num) + previous
                    previous = previousAnswer[i]
                    num = 0
                if i == len(previousAnswer) - 1:
                    answer += str(num + 1) + previous
                    num = 0
                else:
                    num += 1
            holder += 1
            previousAnswer = answer
            answer = ''
            previous = previousAnswer[0]
        return previousAnswer

    def testCountAndSay(self):
        assert self.countAndSay(1) == '1'
        assert self.countAndSay(2) == '11'
        assert self.countAndSay(3) == '21'
        assert self.countAndSay(4) == '1211'
        assert self.countAndSay(5) == '111221'
        assert self.countAndSay(6) == '312211'
        assert self.countAndSay(7) == '13112221'
        assert self.countAndSay(8) == '1113213211'
        assert self.countAndSay(9) == '31131211131221'
        assert self.countAndSay(10) == '13211311123113112211'

if __name__ == '__main__':
    S = Solution()
    S.testCountAndSay()
    print("All Tests Passed")