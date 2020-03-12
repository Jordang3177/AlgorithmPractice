class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        """
        returns the odd values of the matrix after incrementing the given indices by one.
        :param n: int (number of columns that are to be in the matrix)
        :param m: int (number of rows that are to be in the matrix)
        :param indices: List of List of Ints (the indices that are to be incremented by one
        :return: int (The number of odd values in the end matrix)
        """
        matrix = self.makeMatrix(n, m)
        for pairs in indices:
            matrix = self.addToMatrix(pairs, matrix)
        answer = self.findOddValues(matrix)
        return answer

    def makeMatrix(self, n, m):
        output = []
        for i in range(n):
            holder = []
            for j in range(m):
                holder.append(0)
            output.append(holder)
        return output

    def addToMatrix(self, p, matrix):
        firstElement, secondElement = p[0], p[1]
        for i in range(len(matrix[firstElement])):
            matrix[firstElement][i] += 1
        for j in range(len(matrix)):
            matrix[j][secondElement] += 1
        return matrix

    def findOddValues(self, matrix):
        output = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 != 0:
                    output += 1
        return output
