n = int(input())
welfare = list(map(int, input().split(" ")))
max_welfare = max(welfare)
answer = 0
for people in welfare:
    answer += max_welfare - people
print(answer)