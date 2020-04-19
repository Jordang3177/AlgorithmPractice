n = int(input())
for i in range(n):
    buns, beef, chicken = map(int, input().split(" "))
    p_beef, p_chicken = map(int, input().split(" "))
    answer = 0
    if p_beef >= p_chicken:
        max = p_beef
        higher = beef
        min = p_chicken
        lesser = chicken
    else:
        max = p_chicken
        higher = chicken
        min = p_beef
        lesser = beef
    while buns >= 2 and higher:
        buns -= 2
        higher -= 1
        answer += max
    while buns >= 2 and lesser:
        buns -= 2
        lesser -= 1
        answer += min
    print(answer)