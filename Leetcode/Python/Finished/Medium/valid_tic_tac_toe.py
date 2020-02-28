class Solution:
    def validTicTacToe(self, board) -> bool:
        x = 0
        o = 0
        empty = 0
        for item in board:
            for char in item:
                if char == 'X':
                    x += 1
                elif char == 'O':
                    o += 1
                else:
                    empty += 1
        if x - o > 1 or x - o < 0:
            return False
        x_wins = self.checkwinner(board, 'X')
        o_wins = self.checkwinner(board, 'O')
        if x_wins and o_wins:
            return False
        if x_wins and x == o:
            return False
        if x_wins and empty == 0 and x - o != 1:
            return False
        if o_wins and empty == 0:
            return False
        if x_wins:
            return True
        if o_wins:
            return True
        return True

    def checkwinner(self, board, char):
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] == char:
                return True
        for j in range(0, 3):
            if board[0][j] == board[1][j] == board[2][j] == char:
                return True
        if board[0][0] == board[1][1] == board[2][2] == char:
            return True
        if board[0][2] == board[1][1] == board[2][0] == char:
            return True
        return False