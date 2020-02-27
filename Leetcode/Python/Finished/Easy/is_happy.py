class Solution:
    def isHappy(self, n: int) -> bool:
        """
        returns if the number is a happy number. Which means if you add up the squares of each digit over and over will it become 1?
        :param n: int
        :return: bool
        """
        checker = {}
        while n != 1:
            if n in checker:
                return False
            else:
                checker[n] = 1
                answer = 0
                n = str(n)
                for i in range(len(n)):
                    answer += int(n[i]) ** 2
                n = answer
        return True
