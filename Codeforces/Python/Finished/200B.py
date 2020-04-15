n = int(input())
drinks = list(map(int, input().split(" ")))
answer = 0
fraction = 1/ n
for drink in drinks:
    answer += fraction * drink
print(answer)