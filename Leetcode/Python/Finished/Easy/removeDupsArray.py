class Solution:
    def removeDuplicates(self, nums) -> int:
        n = 0
        while(n < len(nums)):
            if len(nums) == 1:
                return 1
            if(nums[n]==nums[n-1]):
                del nums[n]
            else:
                n += 1
        return n


    def test(self):
        assert self.removeDuplicates([1]) == 1
        assert self.removeDuplicates([1,1]) == 1

if __name__ == '__main__':
    S = Solution()
    S.test()
    print("All Tests Passed")