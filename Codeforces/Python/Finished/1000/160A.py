n = int(input())
coins = list(map(int, input().split(" ")))
coins = sorted(coins)
coins = coins[::-1]
half = sum(coins) / 2
answer = 0
holder = 0
i = 0
while holder <= half:
    holder += coins[i]
    answer += 1
    i += 1
print(answer)