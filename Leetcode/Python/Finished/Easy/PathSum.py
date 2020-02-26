class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        """
        returns if there is a path where the node values add up to the parameter sum
        :param root: TreeNode
        :param sum: int
        :return: bool
        """
        if not root:
            return False
        sum = sum - root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)