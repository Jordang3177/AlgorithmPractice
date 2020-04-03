card = input()
cards = list(map(str, input().split(" ")))
found = False
for plays in cards:
    if plays[0] == card[0] or plays[1] == card[1]:
        found = True
if found:
    print("YES")
else:
    print("NO")