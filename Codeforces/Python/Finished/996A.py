money = int(input())
answer = 0
while money > 0:
    if money >= 100:
        money -= 100
        answer += 1
    elif money >= 20:
        money -= 20
        answer += 1
    elif money >= 10:
        money -= 10
        answer += 1
    elif money >= 5:
        money -= 5
        answer += 1
    else:
        money -= 1
        answer += 1
print(answer)