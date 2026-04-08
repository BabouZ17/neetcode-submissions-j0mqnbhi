class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in cols[column]
                    or board[row][column] in rows[row]
                    or board[row][column] in squares[(row//3, column//3)]):
                        return False
                
                cols[column].add(board[row][column])
                rows[row].add(board[row][column])
                squares[(row//3, column//3)].add(board[row][column])
        
        return True