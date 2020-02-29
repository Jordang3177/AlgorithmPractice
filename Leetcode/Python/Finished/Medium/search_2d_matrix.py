class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        """
        returns if the target is in the given matrix
        :param matrix: List of List of Int
        :param target: Int
        :return: bool
        """
        for i in range(len(matrix)):
            if len(matrix[i]) == 0:
                continue
            if matrix[i][len(matrix[i]) - 1] < target:
                continue
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
            break
        return False
