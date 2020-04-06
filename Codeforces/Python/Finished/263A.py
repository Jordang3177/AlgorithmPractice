matrix = []
for i in range(5):
    row = list(map(int, input().split(" ")))
    matrix.append(row)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            row, col = i, j
print(abs(row - 2) + abs(col - 2))