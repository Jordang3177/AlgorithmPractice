import math
n = int(input())
for i in range(n):
    n, a, b = map(int, input().split(' '))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = []
    for k in range(math.ceil(n/a)):
        b_holder = b
        copy_a = alphabet
        holder = ''
        times = 0
        for l in range(a):
            if times == a:
                break
            if len(answer) == n:
                break
            if not b_holder:
                answer.append(holder)
                times += 1
            while b_holder:
                if len(answer) == n:
                    break
                holder = copy_a.pop()
                answer.append(holder)
                b_holder -= 1
                times += 1
    print(''.join(answer))

