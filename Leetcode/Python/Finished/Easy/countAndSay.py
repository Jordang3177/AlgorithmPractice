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
