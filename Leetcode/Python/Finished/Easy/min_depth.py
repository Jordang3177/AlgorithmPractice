class Solution:
    def minDepth(self, root) -> int:
        answer = 1
        if not root:
            return 0
        if not root.left:
            return answer
        if not root.right:
            return answer
        else:
            answer += min(self.minDepth(root.right), self.minDepth(root.left))
            return answer
