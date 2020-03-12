class Solution:
    def countNegatives(self, grid) -> int:
        """
        returns the amount of negative numbers in the given grid that is sorted both row and column wise
        :param grid: List of List of Ints
        :return: Int
        """
        negative_numbers = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    negative_numbers += 1
        return negative_numbers
