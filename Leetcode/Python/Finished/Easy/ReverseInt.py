def reverse(x: int):
    """
    reverses the given number
    :param x: int
    :return: int
    """
    if x < 0:
        signed = True
    else:
        signed = False
    x = str(x)
    if signed:
        x = x[1:]
    x = x[::-1]
    x = int(x)
    if signed:
        x = -x
    if x > 2 ** 31 - 1:
        return 0
    if x < -2 ** 31:
        return 0
    else:
        return x


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