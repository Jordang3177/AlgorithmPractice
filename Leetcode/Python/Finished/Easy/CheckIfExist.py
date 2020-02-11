class Solution:
    def checkIfExist(self, arr):
        if len(arr) <= 1:
            return False
        else:
            for value in arr:
                index = arr.index(value)
                if value*2 in arr[0:index] or value*2 in arr[index+1:len(arr)]:
                    return True
        return False

    def testCheckIfExist(self):
        assert self.checkIfExist([10, 2, 5, 3]) == True
        assert self.checkIfExist([10, 1, 2]) == True
        assert self.checkIfExist([]) == False
        assert self.checkIfExist([1]) == False
        assert self.checkIfExist([1, 2]) == True
        assert self.checkIfExist([1, 1]) == False
        assert self.checkIfExist([1, 3, 5, 7]) == False
        assert self.checkIfExist([7, 1, 14, 11]) == True
        assert self.checkIfExist([-2, 0, 10, -19, 4, 6, -8]) == False

if __name__ == '__main__':
    S = Solution()
    S.testCheckIfExist()
    print("All Tests Passed")
