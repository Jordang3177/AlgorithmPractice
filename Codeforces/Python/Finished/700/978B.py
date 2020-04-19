n = int(input())
string = input()
answer = 0
count = 0
for i in range(len(string)):
    if string[i] != 'x' and count >= 3:
        answer += count - 2
        count = 0
    elif string[i] != 'x':
        count = 0
    elif string[i] == 'x':
        count += 1
if count >= 3:
    answer += count - 2
print(answer)