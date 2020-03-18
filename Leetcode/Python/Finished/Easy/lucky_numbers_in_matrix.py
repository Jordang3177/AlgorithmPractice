class Solution:
    def luckyNumbers (self, matrix):
        answer = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == min(matrix[i]):
                    boolean = True
                    for k in range(len(matrix)):
                        if k == i:
                            continue
                        elif matrix[k][j] > matrix[i][j]:
                            boolean = False
                            break
                    if boolean == True:
                        answer.append(matrix[i][j])
        return answer
