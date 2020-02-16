class Solution:
    def myAtoi(self, str):
        answer = ''
        for char in str:
            if char == ' ':
                str = str[1:len(str)]
            else:
                break
        numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signs = ['+', '-']
        onesign = True
        numberFirst = False
        for i in range(0, len(str)):
            if str[i] in numeric:
                if i == 0:
                    answer += str[i]
                    numberFirst = True
                    continue
                answer += str[i]
                continue
            if str[i] in signs and onesign:
                if i != 0 and numberFirst:
                    break
                answer += str[i]
                onesign = False
            else:
                break
        if len(answer) == 0:
            return 0
        if answer[0] == '+':
            answer = answer[1:len(answer)]
        if len(answer) == 1:
            if answer[0] == '+' or answer[0] == '-':
                return 0
        if len(answer) == 0:
            return 0
        for num in answer:
            if answer[0] == '0':
                answer = answer[1:len(answer)]
            else:
                break
        if len(answer) == 0:
            return 0
        answer = int(answer)
        if answer > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if answer < -2 ** 31:
            return -2 ** 31
        return answer

