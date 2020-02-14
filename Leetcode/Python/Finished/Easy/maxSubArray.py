class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

    def test(self):
        assert self.maxSubArray([1,2,3,4,5]) == 15
        assert self.maxSubArray([-1,1]) == 1
        assert self.maxSubArray([-1,-40,20,33,40,-500,30,4005,-3040,50,4000]) == 5045


if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")
