s = input()
answer = 'NO'
for char in s:
    if char == 'H' or char == 'Q' or char == '9':
        answer = "YES"
        break
print(answer)