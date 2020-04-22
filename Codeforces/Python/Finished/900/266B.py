n, t = map(int, input().split(" "))
s = list(input())
positions = []
for i in range(t):
    j = 0
    while j < len(s) -1:
        if s[j] == 'B' and s[j + 1] == 'G':
            s[j] = 'G'
            s[j + 1] = 'B'
            j += 2
        else:
            j += 1
print(''.join(s))