n = int(input())
string = input()
answer = []
holder = {'z': string.count('z'), 'e': string.count('e'), 'r': string.count('r'), 'o': string.count('o'), 'n': string.count('n')}
if 'n' in holder:
    while holder['n'] != 0:
        answer.append('one')
        holder['o'] -= 1
        holder['n'] -= 1
        holder['e'] -= 1
if 'z' in holder:
    while holder['z'] != 0:
        answer.append('zero')
        holder['z'] -= 1
        holder['e'] -= 1
        holder['r'] -= 1
        holder['o'] -= 1
digits = []
for i in range(len(answer)):
    if answer[i] == 'one':
        digits.append(str(1))
    else:
        digits.append(str(0))
print(' '.join(digits))

