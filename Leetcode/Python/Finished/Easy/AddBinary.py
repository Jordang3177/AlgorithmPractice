class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        i = len(a) - 1
        j = len(b) - 1
        holder = 1
        decA = 0
        decB = 0
        while i >= 0:
            decA = (holder * int(a[i])) + decA
            holder = holder * 2
            i = i - 1
        holder = 1
        while j >= 0:
            decB = (holder * int(b[j])) + decB
            holder = holder * 2
            j = j - 1
        answer = decA + decB
        return self.convertToBinary(answer)

    def convertToBinary(self, num: int) -> str:
        answer = ''
        if num == 0:
            return '0'
        while num != 0:
            answer = str(num % 2) + answer
            num = num // 2
        return answer
