class Solution:
    def plusOne(self, digits):
        """
        given an array representation of a number, returns the array representation of the number plus one
        :param digits: array of ints
        :return: array of ints
        """
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            i = len(digits) - 1
            length = len(digits)
            while digits[i] == 9:
                if i == 0:
                    answer = [1]
                    for i in range(0, length):
                        answer = answer + [0]
                    return answer
                else:
                    digits[i] = 0
                    i = i - 1
            digits[i] += 1
            return digits

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
