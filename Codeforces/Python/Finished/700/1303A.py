n = int(input())
for i in range(n):
    string = input()
    seen = False
    answer = 0
    holder = 0
    for j in range(len(string)):
        if string[j] == '0' and seen:
            holder += 1
        elif string[j] == '1' and seen:
            answer += holder
            holder = 0
        elif string[j] == '1' and not seen:
            seen = True
    print(answer)