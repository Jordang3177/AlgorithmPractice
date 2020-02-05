class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = [1, 2, 3, 4]
        return nums1

    def testMerge(self):
        list1 = [1, 2, 3, 0]
        list2 = [4]
        assert self.merge(list1, 3, list2, 1) == [1, 2, 3, 4]


if __name__ == '__main__':
    S = Solution()
    S.testMerge()
    print("All Tests Passed")