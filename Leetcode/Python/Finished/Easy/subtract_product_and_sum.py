class Solution:
    def subtractProductAndSum(self, n):
        """
        returns the product of the digits minus the sum of the digits
        :param n: int
        :return: int
        """
        str_n = str(n)
        digits = []
        for char in str_n:
            digits.append(int(char))
        product_n = 1
        sum_n = sum(digits)
        for char in digits:
            product_n *= char
        return product_n - sum_n