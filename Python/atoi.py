def myAtoi(str):
    answer = ''
    for char in str:
        if char == ' ':
            str = str[1:len(str)]
        else:
            break
    numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    signs = ['+', '-']
    onesign = True
    numberFirst = True
    for i in range(0, len(str)):
        if str[i] in numeric:
            answer += str[i]
            continue
        if str[i] in signs and onesign:
            answer += str[i]
            onesign = False
        else:
            break
    if len(answer) == 0:
        return 0
    if answer[0] == '+':
        answer = answer[1:len(answer)]
    if len(answer) == 1:
        if answer[0] == '+' or answer[0] == '-':
            return 0
    if len(answer) == 0:
        return 0
    for num in answer:
        if answer[0] == '0':
            answer = answer[1:len(answer)]
        else:
            break
    if len(answer) == 0:
        return 0
    answer = int(answer)
    if answer > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if answer < -2 ** 31:
        return -2 ** 31
    return answer

def test_myAtoi():
    assert myAtoi('42') == 42
    assert myAtoi('3439') == 3439
    assert myAtoi('-13') == -13
    assert myAtoi("   -42") == -42
    assert myAtoi('       wow a 123') == 0
    assert myAtoi('wow a 123') == 0
    assert myAtoi('    123') == 123
    assert myAtoi('     wow a -123') == 0
    assert myAtoi('-23434399539583843') == -2**31
    assert myAtoi('23433885738963863') == 2**31 - 1
    assert myAtoi('-1+') == -1
    assert myAtoi('+-2') == 0
    assert myAtoi('-+2') == 0
    assert myAtoi('0000000') == 0
    assert myAtoi('     00000   ') == 0
    assert myAtoi('0-1') == 0
    assert myAtoi('    0-1') == 0
    assert myAtoi('0+1') == 0
    assert myAtoi('     0+1') == 0

if __name__ == "__main__":
    test_myAtoi()
    print("All Tests Passed")