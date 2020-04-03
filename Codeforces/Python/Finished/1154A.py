x = input()
x = list(map(int, x.split(" ")))
x.sort()
print(str(x[3] - x[0]) + " " + str(x[3] - x[1]) + " " + str(x[3] - x[2]))