class Solution:
    def generate(self, numRows: int):
        """
        returns pascal's triangle with height of numRows
        :param numRows: int
        :return: Array of Array of Ints (2D Array of Ints)
        """
        answer = []
        for rows in range(numRows):
            row = []
            for i in range(rows + 1):
                row.append(None)
            row[0], row[len(row) -1] = 1,1
            for j in range(1, len(row) - 1):
                row[j] = answer[rows-1][j-1] + answer[rows-1][j]
            answer.append(row)
        return answer