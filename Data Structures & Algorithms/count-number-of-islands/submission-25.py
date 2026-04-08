from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(0, ROWS) and
                        nc in range(0, COLS) and
                        grid[nr][nc] == "1"
                    ):
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


