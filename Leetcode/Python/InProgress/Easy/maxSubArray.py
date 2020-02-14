class Solution:
    def maxSubArray(self, nums):
        return 1

    def test(self):
        assert self.maxSubArray([1,2,3,4,5]) == 13
        assert self.maxSubArray([-1,1]) == 1


if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")
