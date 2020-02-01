# This algorithm got faster than 93% of people in speed and 94% of people in memory space.
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0
        else:
            for i in range(0, len(nums)):
                if target > nums[i] and target < nums[i+1]:
                    return i + 1

    def testsearchInsert(self):
        assert self.searchInsert([1, 3, 5, 6], 5) == 2
        assert self.searchInsert([1, 3, 5, 6], 2) == 1
        assert self.searchInsert([1, 3, 5, 6], 7) == 4
        assert self.searchInsert([1, 3, 5, 6], 0) == 0


if __name__ == '__main__':
    S = Solution()
    S.testsearchInsert()
    print("All Tests Passed")