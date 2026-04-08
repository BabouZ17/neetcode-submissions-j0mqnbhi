class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            print(r,c, visited)
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r,c) in visited
                or grid[r][c] == 0
            ):
                return 0

            visited.add((r,c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea