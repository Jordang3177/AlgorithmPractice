n = int(input())
bus = []
answer = ''
for i in range(n):
    row = [char for char in input()]
    bus.append(row)
for row in bus:
    if answer == 'YES':
        break
    for j in range(len(row)):
        if j == len(row) - 1:
            continue
        elif row[j] == 'O' and row[j + 1] == 'O':
            row[j] = '+'
            row[j + 1] = '+'
            answer = 'YES'
            break
if answer == '':
    answer = 'NO'
print(answer)
if answer == 'YES':
    for k in range(len(bus)):
        print(''.join(bus[k]))