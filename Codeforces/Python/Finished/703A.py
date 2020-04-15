n = int(input())
m = 0
c = 0
for i in range(n):
    mi, ci = map(int, input().split(" "))
    if mi > ci:
        m += 1
    if ci > mi:
        c += 1
if m > c:
    print('Mishka')
if c > m:
    print('Chris')
if c == m:
    print("Friendship is magic!^^")