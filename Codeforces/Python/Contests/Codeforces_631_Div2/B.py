t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split(" ")))
    answer = 0
    lengths = []
    dictionary = {}
    for j in range(n):
        first_half = set(array[0:j])
        second_half = set(array[j:len(array)])
        # print(first_half)
        # print(j)
        # print(second_half)
        # print(j - n)
        if len(first_half) != j or len(second_half) != (n - j):
            # print('continue')
            continue
        first = True
        second = True
        for k in range(1, len(first_half) + 1):
            if k in first_half:
                continue
            else:
                first = False
                break
        # print('First ' + str(first))
        for l in range(1, len(second_half) + 1):
            if l in second_half:
                continue
            else:
                second = False
                break
        if first and second:
            answer += 1
            lengths.append((len(first_half), len(second_half)))
            dictionary[first_half] = second_half
    print(answer)
    for m in range(len(lengths)):
        print(' '.join(list(map(str, lengths[m]))))