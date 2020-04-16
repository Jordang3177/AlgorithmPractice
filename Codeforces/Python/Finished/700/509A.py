n = int(input())
answer = 0
matrix = []
for i in range(n):
    if i == 0:
        holder = [1] * n
        matrix.append(holder)
    else:
        holder = []
        for j in range(n):
            if j == 0:
                holder.append(1)
            else:
                current = holder[j - 1] + matrix[i-1][j]
                holder.append(current)
        matrix.append(holder)
print(matrix[n-1][n-1])