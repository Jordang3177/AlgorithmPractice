n = int(input())
string = input()
cipher = []
for i in range(n):
    cipher.append(string[0])
    if i+1 >= len(string):
        break
    string = string[i+1:len(string)]
print("".join(cipher))