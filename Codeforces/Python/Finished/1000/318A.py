n, m = map(int, input().split(" "))
holder = []
for i in range(1, n+1, 2):
    holder.append(i)
for j in range(2, n+1, 2):
    holder.append(j)
print(holder[m-1])