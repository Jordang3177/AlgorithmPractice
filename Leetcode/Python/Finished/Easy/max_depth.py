class Solution:
    def maxDepth(self, root) -> int:
        answer = 1
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            answer += self.maxDepth(root.right)
        elif not root.right:
            answer += self.maxDepth(root.left)
        else:
            answer += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return answer