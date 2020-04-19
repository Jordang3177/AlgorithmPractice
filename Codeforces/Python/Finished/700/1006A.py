n = int(input())
numbers = list(map(int, input().split(" ")))
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] -= 1
print(' '.join(map(str, numbers)))