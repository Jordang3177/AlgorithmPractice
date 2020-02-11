class Solution():
    def diag(self, arr):
            left = 0
            right = 0
            j = len(arr) - 1
            for i in range(0, len(arr)):
                left += arr[i][i]
                right += arr[i][j]
                j -= 1
            return abs(left - right)

    def testDiag(self):
        assert self.diag([[1,2,3],
                          [4,5,6],
                          [7,8,9]]) == 0
        assert self.diag([[1,1,1,2],
                          [1,1,1,2],
                          [1,1,1,2],
                          [1,1,1,2]]) == 0
        assert self.diag([[1,2,3,4],
                          [5,6,7,8],
                          [9,10,11,12],
                          [13,14,15,16]]) == abs((1+6+11+16) - (4+7+10+13))
        assert self.diag([[1,2,1,2,1],
                          [1,2,1,2,1],
                          [1,2,1,2,1],
                          [1,2,1,2,1],
                          [1,2,3,4,5]]) == abs((1+2+1+2+5) - (1+2+1+2+1))
if __name__ == '__main__':
    S = Solution()
    S.testDiag()
    print("All Tests Passed")