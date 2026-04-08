class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visited
                or grid[r][c] == "0"
            ):
                return
            
            visited.add((r,c))
            drs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dc, dr in drs:
                dfs(r+dr, c+dc)
                
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col)
                    islands += 1
        return islands