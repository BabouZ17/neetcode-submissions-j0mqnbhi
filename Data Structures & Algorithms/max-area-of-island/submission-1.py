class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == 0
                or (r,c) in visited
            ):
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                area = max(area, dfs(row, col))
        return area