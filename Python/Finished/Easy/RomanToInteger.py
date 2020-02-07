def romanToInt(s):
    answer = 0
    while len(s) > 0:
        if len(s) > 1:
            if s[0] == 'I' and s[1] == 'V':
                answer += 4
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'I' and s[1] == 'X':
                answer += 9
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'X' and s[1] == 'L':
                answer += 40
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'X' and s[1] == 'L':
                answer += 90
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'C' and s[1] == 'D':
                answer += 400
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'C' and s[1] == 'M':
                answer += 900
                if len(s) > 2:
                    s = s[2:len(s)]
                    continue
                else:
                    return answer
        if len(s) > 0:
            if s[0] == 'I':
                answer += 1
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'V':
                answer += 5
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'X':
                answer += 10
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'L':
                answer += 50
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'C':
                answer += 100
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'D':
                answer += 500
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
            if s[0] == 'M':
                answer += 1000
                if len(s) > 1:
                    s = s[1:len(s)]
                    continue
                else:
                    return answer
    else:
        return answer

print(romanToInt('III'))