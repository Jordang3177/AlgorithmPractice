n = int(input())
numbers = list(map(int, input().split(" ")))
holder = {}
for i in range(len(numbers)):
    holder[i + 1] = numbers[i]
answer = [0] * n
for key, value in holder.items():
    answer[value - 1] = str(key)
print(' '.join(answer))