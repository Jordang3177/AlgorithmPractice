k, n, w = map(int, input().split(" "))
answer = 0
for i in range(1, w+1):
    answer += k * i
holder = answer - n
if holder <= 0:
    print(0)
else:
    print(holder)