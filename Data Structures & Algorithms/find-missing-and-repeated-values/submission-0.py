class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = 0
        seen = set()
        a = b = -1

        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if val in seen:
                    a = val
                seen.add(grid[r][c])

        b = sum(range(n*n + 1)) - sum(seen)
        return [a, b]