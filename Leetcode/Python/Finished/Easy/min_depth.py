class Solution:
    def minDepth(self, root) -> int:
        answer = 1
        if not root:
            return 0
        if not root.left:
            answer += self.minDepth(root.right)
            return answer
        if not root.right:
            answer += self.minDepth(root.left)
            return answer
        else:
            answer += min(self.minDepth(root.right), self.minDepth(root.left))
            return answer
