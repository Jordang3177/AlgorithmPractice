class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 5 == 0:
                answer.append('Buzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            else:
                stri = str(i)
                answer.append(stri)
        return answer