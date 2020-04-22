s1 = input()
s2 = input()
s1_count = 0
s2_count = 0
for i in range(len(s1)):
    char1 = s1[i].lower()
    char2 = s2[i].lower()
    s1_count += ord(char1)
    s2_count += ord(char2)
    if s1_count > s2_count:
        print(1)
        break
    elif s2_count > s1_count:
        print(-1)
        break
if s1_count == s2_count:
    print(0)