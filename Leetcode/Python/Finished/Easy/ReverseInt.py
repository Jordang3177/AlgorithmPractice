def reverse(x: int):
    """
    reverses the given number
    :param x: int
    :return: int
    """
    if x == '':
        return 0
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    y = str(x)
    answer = ''
    if y[0] == '-':
        y = y[1:len(y)]
    for num in y:
        answer += y[len(y) - 1]
        y = y[0:len(y) - 1]
    for num in answer:
        if answer[0] == 0:
            answer = answer[1:len(answer)]
        else:
            break
    answer = int(answer)
    if x < 0:
        answer = answer * -1
    if answer > 2 ** 31 - 1 or answer < -2 ** 31:
        return 0
    return answer


def test_reverse():
    assert reverse(-123) == -321
    assert reverse(123) == 321
    assert reverse(123456789) == 987654321
    assert reverse(100000) == 1
    assert reverse(-21448484858680600) == 0
    assert reverse(203340304303030) == 0
    assert reverse(2**31) == 0
    assert reverse(-2**31 -1) == 0

if __name__ == "__main__":
    test_reverse()
    print("All Tests Passed")