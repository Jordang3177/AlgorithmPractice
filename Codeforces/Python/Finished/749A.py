n = int(input())
answer = 0
numbers = []
if n % 2 == 0:
    while n:
        n -= 2
        numbers.append(str(2))
        answer += 1
else:
    while n > 3:
        n -= 2
        numbers.append(str(2))
        answer += 1
    if n == 3:
        n -= 3
        numbers.append(str(3))
        answer += 1
print(answer)
print(' '.join(numbers))