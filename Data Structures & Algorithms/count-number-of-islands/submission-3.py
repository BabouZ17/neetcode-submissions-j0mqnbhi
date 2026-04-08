class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r,c) in visited
                or grid[r][c] == "0"
            ):
                return
            
            visited.add((r,c))
            drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in drs:
                dfs(r+dr, c+dc)

        islands = 0
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                   islands += 1
                   dfs(r,c)
        return islands 



