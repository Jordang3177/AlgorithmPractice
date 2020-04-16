n = int(input())
answer = []
for i in range(1, n+1):
    if i % 2 == 0:
        answer.append("I love ")
    else:
        answer.append("I hate ")
    if i == n:
        answer.append("it")
    if i != n:
        answer.append("that ")

print(''.join(answer))