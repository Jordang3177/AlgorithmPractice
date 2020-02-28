class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        returns the hamming distance between the two integers
        :param x: int
        :param y: int
        :return: int
        """
        bx = ''
        by = ''
        while x != 0:
            bx = str(x % 2) + bx
            x = x // 2
        while y != 0:
            by = str(y % 2) + by
            y = y // 2
        count = 0
        if len(bx) > len(by):
            difference = len(bx) - len(by)
            count += bx[0:difference].count('1')
            bx = bx[difference:len(bx)]
        if len(by) > len(bx):
            difference = len(by) - len(bx)
            count += by[0:difference].count('1')
            by = by[difference:len(by)]
        for i in range(len(bx)):
            if bx[i] != by[i]:
                count += 1
        return count