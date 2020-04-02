k = int(input())
shapes = []
for i in range(k):
    shapes.append(input())
answer = 0
for i in range(len(shapes)):
    if shapes[i][0] == 'T':
        answer += 4
    if shapes[i][0] == 'C':
        answer += 6
    if shapes[i][0] == 'O':
        answer += 8
    if shapes[i][0] == 'D':
        answer += 12
    if shapes[i][0] == 'I':
        answer += 20
print(answer)
