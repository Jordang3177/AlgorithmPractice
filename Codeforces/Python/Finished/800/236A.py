s = input()
count = set()
for char in s:
    count.add(char)
if len(count) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")