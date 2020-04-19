import math
n = int(input())
for i in range(n):
    a, b, k = map(int, input().split(" "))
    answer = 0
    times_a = math.ceil(k / 2)
    times_b = math.floor(k / 2)
    answer += a * times_a
    answer -= b * times_b
    print(answer)