class Solution:
    def plusOne(self, digits):
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            i = len(digits - 1)
            while digits

    def testPlusOne(self):
        assert self.plusOne([1,2,3]) == [1,2,4]
        assert self.plusOne([0]) == [1]
        assert self.plusOne([1]) == [2]
        assert self.plusOne([9]) == [1,0]
        assert self.plusOne([1,0,9]) == [1,1,0]
        assert self.plusOne([9,9,9]) == [1,0,0,0]

if __name__ == "__main__":
    S = Solution()
    S.testPlusOne()
    print("All Tests Passed")
