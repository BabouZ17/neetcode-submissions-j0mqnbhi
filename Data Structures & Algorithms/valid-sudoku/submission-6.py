from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                ROW, COL = r // 3, c // 3
                if board[r][c] == ".":
                    continue
                
                if (
                    board[r][c] in rows[r] or 
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(ROW, COL)]
                ):
                    return False

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(ROW, COL)].add(board[r][c])

        return True