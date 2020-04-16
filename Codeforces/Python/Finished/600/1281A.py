n = int(input())
for i in range(n):
    s = input()
    if s[len(s)-2:len(s)] == 'po':
        print('FILIPINO')
    elif s[len(s)-5:len(s)] == 'mnida':
        print('KOREAN')
    else:
        print('JAPANESE')