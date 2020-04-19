n = int(input())
coins = list(map(int, input().split(" ")))
dict = {}
for coin in coins:
    if coin in dict:
        dict[coin] += 1
    else:
        dict[coin] = 1
print(max(dict.values()))