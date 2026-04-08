class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= ROWS or
                c >= COLS or
                (r,c) in visit or
                grid[r][c] == "0"
            ):
                return
            
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            return

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands