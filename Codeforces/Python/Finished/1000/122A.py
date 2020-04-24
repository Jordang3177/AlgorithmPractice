n = int(input())
str_n = str(n)
list_n = list(str_n)
answer = False
for i in range(n + 1):
    str_i = str(i)
    list_i = list(str_i)
    holder = True
    for char in list_i:
        if char != '4' and char != '7':
            holder = False
            break
    if holder and n % i == 0:
        answer = True
if answer:
    print("YES")
else:
    print("NO")