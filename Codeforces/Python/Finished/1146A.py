import math
s = input()
a = s.count('a')
if a > math.ceil(len(s)/2):
    print(len(s))
else:
    print(a * 2 - 1)