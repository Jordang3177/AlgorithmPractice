n, h = map(int, input().split(" "))
people = list(map(int, input().split(" ")))
answer = 0
for person in people:
    if person <= h:
        answer += 1
    else:
        answer += 2
print(answer)
