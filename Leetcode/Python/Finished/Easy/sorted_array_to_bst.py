class Solution:
    def sortedArrayToBST(self, nums):
        """
        takes the sorted array nums and turns it into a binary search tree
        :param nums: array of ints
        :return: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        return self.sortedArrayToBSTRecursion(nums, 0, len(nums) - 1)

    def sortedArrayToBSTRecursion(self, nums, left, right):
        """
        finds the middle of the given array nums and then creates a new node with that middle.
        :param nums: array of ints
        :param left: int
        :param right: int
        :return: TreeNode
        """
        if left > right:
            return None
        mid = left + (right - left) // 2
        current = TreeNode(nums[mid])
        current.left = self.sortedArrayToBSTRecursion(nums, left, mid - 1)
        current.right = self.sortedArrayToBSTRecursion(nums, mid + 1, right)
        return current