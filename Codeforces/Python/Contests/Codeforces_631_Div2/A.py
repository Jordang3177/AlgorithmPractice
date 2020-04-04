t = int(input())
for i in range(t):
    n, x = input().split(" ")
    n, x = int(n), int(x)
    array = list(map(int, input().split(" ")))
    array = set(array)
    j = 1
    while x != 0:
        if j in array:
            j += 1
            continue
        else:
            array.add(j)
            x -= 1
            j += 1
    answer = 0
    k = 1
    while True:
        if k in array:
            answer += 1
            k += 1
        else:
            break
    print(answer)