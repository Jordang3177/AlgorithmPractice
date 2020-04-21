n = int(input())
answer = 0
for i in range(n):
    row = list(map(int, input().split(" ")))
    s = sum(row)
    if s >= 2:
        answer += 1
print(answer)