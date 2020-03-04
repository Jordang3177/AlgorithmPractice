class Solution:
    def thirdMax(self, nums):
        """
        returns the third max of the given nums array
        :param nums: Array of Int
        :return: int
        """
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        for i in range(2):
            nums.remove(max(nums))
        return max(nums)
