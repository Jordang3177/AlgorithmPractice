class Solution:
    def threeSum(self, nums):
        return []

    def testThreeSum(self):
        assert self.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1],[-1,-1,2]]


if __name__ == '__main__':
    S = Solution()
    S.testThreeSum()
    print("All Tests Passed")
