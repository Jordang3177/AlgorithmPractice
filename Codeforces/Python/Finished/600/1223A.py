n = int(input())
for i in range(n):
    x = int(input())
    if x <= 4:
        print(4 - x)
    elif x % 2 == 0:
        print(0)
    else:
        print(1)