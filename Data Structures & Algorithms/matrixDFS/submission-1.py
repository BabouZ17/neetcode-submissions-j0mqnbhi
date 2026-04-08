class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                grid[r][c]
            ):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visited.add((r, c))

            res = 0
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            visited.remove((r, c))
            return res

        return dfs(0, 0)