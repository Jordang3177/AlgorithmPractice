n = int(input())
s = input()
answer = 0
previous = s[0]
for i in range(1, len(s)):
    if s[i] == previous:
        answer += 1
        previous = s[i]
    else:
        previous = s[i]
print(answer)