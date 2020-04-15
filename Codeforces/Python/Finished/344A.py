n = int(input())
previous = "00"
answer = 0
for i in range(n):
    current = input()
    if current != previous:
        answer += 1
    previous = current
print(answer)