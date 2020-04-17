n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    answer = 0
    c = b - a
    if a == b:
        print(0)
    elif c >= 0 and c % 2 != 0:
        print(1)
    elif c >= 0 and c % 2 == 0:
        print(2)
    elif c < 0 and c % 2 != 0:
        print(2)
    else:
        print(1)
