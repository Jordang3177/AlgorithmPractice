class Solution:
    def getRow(self, rowIndex):
        """
        returns the given row of pascal's triangle
        :param rowIndex: int
        :return: Array of Int
        """
        answer = []
        for rows in range(rowIndex + 1):
            row = []
            for i in range(rows + 1):
                row.append(None)
            row[0], row[len(row) - 1] = 1, 1
            for j in range(1, len(row) -1):
                row[j] = answer[rows-1][j-1] + answer[rows-1][j]
            answer.append(row)
        return answer[rowIndex]