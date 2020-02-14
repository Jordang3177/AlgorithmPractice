class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        prev_answer = '1'
        current_number = prev_answer[0]
        answer = ''
        counter = 0
        for i in range(1, n):
            for j in range(0, len(prev_answer)):
                if current_number != prev_answer[j]:
                    answer += str(counter) + current_number
                    counter = 0
                    current_number = prev_answer[j]
                if j == len(prev_answer) - 1:
                    answer += str(counter + 1) + current_number
                    counter = 0
                else:
                    counter += 1
            prev_answer = answer
            answer = ''
            current_number = prev_answer[0]
        return prev_answer

    def test(self):
        assert self.countAndSay(1) == '1'
        assert self.countAndSay(2) == '11'
        assert self.countAndSay(3) == '21'
        assert self.countAndSay(4) == '1211'
        assert self.countAndSay(5) == '111221'
        assert self.countAndSay(6) == '312211'
        assert self.countAndSay(7) == '13112221'

if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")