class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Returns the hamming weight of the given int (The number of 1 bits in the binary representation of the int)
        :param n: int
        :return: int
        """
        answer = ''
        while n > 0:
            answer = str(n % 2) + answer
            n = n // 2
        count = 0
        for i in range(len(answer)):
            count += int(answer[i])
        return count
