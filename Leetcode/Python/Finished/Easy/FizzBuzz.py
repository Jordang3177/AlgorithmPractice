class Solution:
    def fizzBuzz(self, n):
        """
        returns an array of elements for FizzBuzz question up to and including N
        :param n: int
        :return: array
        """
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 5 == 0:
                answer.append('Buzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            else:
                answer.append(str(i))
        return answer