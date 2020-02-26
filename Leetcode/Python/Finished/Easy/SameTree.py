class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


class Solution:
    def same_tree(self, p, q):
        """
        Checks if both given Treenodes are the same
        :param p: TreeNode
        :param q: TreeNode
        :return: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)