n = int(input())
answer = 0
for i in range(1, int(n / 2) + 1):
    holder = n - i
    if holder % i == 0:
        answer += 1
print(answer)