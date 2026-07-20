class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        a = b = 0

        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if val in seen:
                    a = val
                seen.add(grid[r][c])

        for val in range(1, n * n + 1):
            if val not in seen:
                b = val
                break

        return [a, b]