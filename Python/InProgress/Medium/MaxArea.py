class Solution:
    def maxArea(self, height):
        return 1

    def testMaxArea(self):
        assert self.maxArea([[1, 8, 6, 2, 5, 4, 8, 3, 7]]) == 49


if __name__ == '__main__':
    S = Solution()
    S.testMaxArea()
    print("All Tests Passed")
