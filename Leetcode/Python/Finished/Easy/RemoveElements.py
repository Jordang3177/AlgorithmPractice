class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

    def test(self):
        assert self.removeElement([1,2,3,4], 3) == 3
        assert self.removeElement([1,1,1,1,1,1], 1) == 0
        assert self.removeElement([1,2,3,4,4,4,4,4], 4) == 3

if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")