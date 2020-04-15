n = int(input())
for i in range(n):
    holder = []
    for j in range(9):
        row = list(map(int, input()))
        holder.append(row)
    for k in range(len(holder)):
        if holder[k][k] == 9:
            holder[k][k] = 8
        else:
            holder[k][k] = holder[k][k] + 1
    for l in range(len(holder)):
        hold = list(map(str, holder[l]))
        print(''.join(hold))

