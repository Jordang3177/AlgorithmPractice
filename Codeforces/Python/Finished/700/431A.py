cals = list(map(int, input().split(" ")))
game = input()
answer = 0
for char in game:
    answer += cals[int(char) - 1]
print(answer)