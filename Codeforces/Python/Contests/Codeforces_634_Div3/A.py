n = int(input())
for i in range(n):
    candies = int(input())
    if candies % 2 == 0:
        answer = int(candies / 2)
        answer -= 1
    else:
        answer = int(candies / 2)
    print(answer)