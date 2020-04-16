younger, older = map(int, input().split(" "))
answer = 0
while younger <= older:
    younger *= 3
    older *= 2
    answer += 1
print(answer)
