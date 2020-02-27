class Solution:
    def isValidSudoku(self, board) -> bool:
        return self.checkrows(board) and self.checkcolumns(board) and self.checkboxes(board)

    def checkrows(self, board):
        for i in range(len(board)):
            seen = {}
            for j in range(len(board[i])):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                else:
                    seen[board[i][j]] = 1
        return True

    def checkcolumns(self, board):
        for i in range(len(board[0])):
            seen = {}
            for j in range(len(board)):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                else:
                    seen[board[j][i]] = 1
        return True

    def checkboxes(self, board):
        for sub in range(9):
            seen = {}
            for i in range(3):
                for j in range(3):
                    holderi = ((sub // 3) * 3) + i
                    holderj = ((sub % 3) * 3) + j
                    if board[holderi][holderj] in seen and board[holderi][holderj] != '.':
                        return False
                    else:
                        seen[board[holderi][holderj]] = 1
        return True
