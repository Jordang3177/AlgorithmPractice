s = list(input())
i = 0
while i < len(s):
    if s[i] == '+':
        s.pop(i)
    else:
        i += 1
s.sort()
print('+'.join(s))