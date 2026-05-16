class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])

        res = [[0] * n for _ in range(m)]
        for r in range(m):
            for i in range(k):
                if mat1[r][i]:
                    val = mat1[r][i]
                    for c in range(n):
                        res[r][c] += val * mat2[i][c]
        return res