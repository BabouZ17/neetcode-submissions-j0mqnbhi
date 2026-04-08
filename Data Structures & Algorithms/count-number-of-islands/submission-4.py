class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r,c):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == "0"
                or (r,c) in visited
            ):
                return
            
            visited.add((r,c))
            for dr, dc in drs:
                dfs(r+dr, c+dc)

        islands = 0
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                   dfs(r,c)
                   islands += 1
        return islands 



