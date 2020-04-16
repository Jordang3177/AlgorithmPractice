n, m = map(int, input().split(" "))
s = input().split(" ")
t = input().split(" ")
q = int(input())
for i in range(q):
    y = int(input())
    first = (y % n) - 1
    second = (y % m) - 1
    answer = s[first] + t[second]
    print(answer)
