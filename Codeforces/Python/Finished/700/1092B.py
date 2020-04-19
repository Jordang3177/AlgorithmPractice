n = int(input())
players = list(map(int, input().split(" ")))
players.sort()
answer = 0
for i in range(0, len(players), 2):
    answer += players[i + 1] - players[i]
print(answer)