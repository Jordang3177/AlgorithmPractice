class Solution:
    def searchInsert(self, nums, target):
        return 'wow'

    def testsearchInsert(self):
        assert self.searchInsert([1,3,5,6], 5) == 2
        assert self.searchInsert([1,3,5,6], 2) == 1
        assert self.searchInsert([1,3,5,6], 7) == 4
        assert self.searchInsert([1,3,5,6], 0) == 0


if __name__ == '__main__':
    S = Solution()
    S.testsearchInsert()
    print("All Tests Passed")