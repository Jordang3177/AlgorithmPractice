n = int(input())
answer = 0
for i in range(n):
    s = input()
    if '+' in s:
        answer += 1
    else:
        answer -= 1
print(answer)