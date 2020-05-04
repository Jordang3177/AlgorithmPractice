class Solution:
    def findComplement(self, num: int) -> int:
        answer = []
        while num > 0:
            if num % 2 == 1:
                answer.append(1)
            else:
                answer.append(0)
            num = num // 2
        complement = 0
        for i in range(len(answer)):
            if answer[i] == 1:
                complement += 0 * 2 ** i
            else:
                complement += 1 * 2 ** i
        return complement