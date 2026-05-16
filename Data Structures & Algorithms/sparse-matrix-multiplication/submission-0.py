class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat1), len(mat2[0])
        k = len(mat1[0])

        res = [[0  for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                res[r][c] = sum([mat1[r][i] * mat2[i][c] for i in range(k)])
        return res