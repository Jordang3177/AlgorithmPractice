class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) != m:
            nums1.pop(m)
        i = 0
        while len(nums2) != 0:
            if i == len(nums1):
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            elif nums1[i] >= nums2[0]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
                i += 1
            else:
                i += 1