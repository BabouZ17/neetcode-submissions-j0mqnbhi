from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        ROWS = COLS = 9

        for r in range(ROWS):
            for c in range(COLS):
                value = board[r][c]
                if (
                    value in rows[r] or
                    value in cols[c] or
                    value in squares[(r//3, c//3)]
                ) and value != ".":
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r//3, c//3)].add(value)
        return True