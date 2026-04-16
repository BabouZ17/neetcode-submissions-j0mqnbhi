class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 2 else -1

        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer

        if row == col:
            self.diagonal += currentPlayer

        if col == (len(self.cols) - row - 1):
            self.antidiagonal += currentPlayer

        n = len(self.rows)

        if (abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.diagonal) == n or
            abs(self.antidiagonal) == n
        ):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
