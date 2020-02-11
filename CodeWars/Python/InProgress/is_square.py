class Solution():
    def is_square(self, n):
        if n < 0:
            return False
        elif n == 0:
            return True
        else:
            factor = n ** (1/2)
            if n % factor == 0:
                return True
            else:
                return False

    def test_is_square(self):
        assert(self.is_square(-1)) == False
        assert(self.is_square(0)) == True
        assert(self.is_square(3)) == False
        assert(self.is_square(4)) == True
        assert(self.is_square(25)) == True
        assert(self.is_square(26)) == False

if __name__ == '__main__':
    S = Solution()
    S.test_is_square()
    print("All Tests Passed")