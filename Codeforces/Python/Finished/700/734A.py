n = int(input())
string = input()
a = 0
d = 0
for char in string:
    if char == "A":
        a += 1
    if char == "D":
        d += 1
if a == d:
    print('Friendship')
if a > d:
    print('Anton')
if d > a:
    print('Danik')