class Solution:
    def findComplement(self, num: int) -> int:
        answer = []
        while num > 0:
            if num % 2 == 1:
                answer.append(0)
            else:
                answer.append(1)
            num = num // 2
        complement = 0
        for i in range(len(answer)):
            complement += answer[i] * 2 ** i
        return complement

