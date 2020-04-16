n = int(input())
drinks = list(map(int, input().split(" ")))
percentage = 0
fraction = 1/ n
for drink in drinks:
    percentage += fraction * drink
print(percentage)