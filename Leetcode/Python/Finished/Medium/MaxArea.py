class Solution:
    def maxArea(self, height):
        answer = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 != p2:
            if height[p1] < height[p2]:
                answer = max(answer, abs(p1 - p2) * height[p1])
                p1 += 1
            else:
                answer = max(answer, abs(p1 - p2) * height[p2])
                p2 -= 1
        return answer

    def testMaxArea(self):
        assert self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


if __name__ == '__main__':
    S = Solution()
    S.testMaxArea()
    print("All Tests Passed")
