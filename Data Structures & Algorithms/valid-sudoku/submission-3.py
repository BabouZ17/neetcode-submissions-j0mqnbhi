class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        cols = [[[] for _ in range(ROWS)] for _ in range(COLS)]

        # compute columns
        for i in range(ROWS):
            for j in range(COLS):
                cols[j][i] = board[i][j]

        # computes squares
        squares = [[[] for _ in range(int(ROWS/3))] for _ in range(int(COLS/3))]
        for i in range(ROWS):
            for j in range(COLS):
                squares[i//3][j//3].append(board[i][j])

        for i in range(ROWS):
            for j in range(COLS):
                value = board[i][j]
                if (
                    value in board[i][:j] or
                    value in board[i][j+1:] or 
                    value in cols[j][:i] or
                    value in cols[j][i+1:] or
                    squares[i//3][j//3].count(value) > 1
                ) and value != ".":
                    return False

        return True