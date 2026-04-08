class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def memoization(r: int, c: int, m: int, n: int, cache: List[List[int]]) -> int:
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n -1:
                return 1

            cache[r][c] = memoization(r+1, c, m, n, cache) + memoization(r, c+1, m, n, cache)
            return cache[r][c]
        return memoization(0, 0, m, n, [[0] * n for _ in range(m)])