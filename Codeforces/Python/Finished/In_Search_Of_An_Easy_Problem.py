k = map(int, input())
answers = list(map(int, input().split(" ")))
max = max(answers)
if max == 1:
    print("HARD")
else:
    print("EASY")