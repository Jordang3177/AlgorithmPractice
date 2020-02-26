class Solution:
    def isSymmetric(self, root) -> bool:
        """
        returns if the given tree is symmetric
        :param root: TreeNode
        :return: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        """
        determines if the two trees are the mirror images of each other
        :param t1: TreeNode
        :param t2: TreeNode
        :return: bool
        """
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
