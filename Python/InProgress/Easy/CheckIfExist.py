class Solution:
    def checkIfExist(self, arr):
        return True

    def testCheckIfExist(self):
        assert self.checkIfExist([10, 2, 5, 3]) == True
        assert self.checkIfExist([10, 1, 2]) == True
        assert self.checkIfExist([]) == False
        assert self.checkIfExist([1]) == False
        assert self.checkIfExist([1,2]) == True
        assert self.checkIfExist([1,1]) == False
        assert self.checkIfExist([1,3,5,7]) == False
        assert self.checkIfExist([7, 1, 14, 11]) == True

if __name__ == '__main__':
    S = Solution()
    S.testCheckIfExist()
    print("All Tests Passed")
