def intToRoman(num):
    answer = ""
    while num > 0:
        if num >= 1000:
            answer += 'M'
            num = num - 1000
        elif num >= 900:
            answer = answer + 'CM'
            num = num - 900
        elif num >= 500:
            answer = answer + 'D'
            num = num - 500
        elif num >= 400:
            answer = answer + 'CD'
            num = num - 400
        elif num >= 100:
            answer = answer + 'C'
            num = num - 100
        elif num >= 90:
            answer = answer + 'XC'
            num = num - 90
        elif num >= 50:
            answer = answer + 'L'
            num = num - 50
        elif num >= 40:
            answer = answer + 'XL'
            num = num - 40
        elif num >= 10:
            answer = answer + 'X'
            num = num - 10
        elif num >= 9:
            answer = answer + 'IX'
            num = num - 9
        elif num >= 5:
            answer = answer + 'V'
            num = num - 5
        elif num >= 4:
            answer = answer + 'IV'
            num = num - 4
        elif num >= 1:
            answer = answer + 'I'
            num = num - 1
    return answer

intToRoman(1111)
intToRoman(4)
intToRoman(9999)