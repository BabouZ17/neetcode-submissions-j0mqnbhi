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

        for num in range(1, n*n + 1):
            if num not in seen:
                b = num
                break
        return [a, b]