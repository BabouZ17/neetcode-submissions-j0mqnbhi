from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = 0
            res = 1
            
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr == ROWS or 
                        nc == COLS or
                        grid[nr][nc] == 0
                    ):
                        continue
                    res += 1
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
            return res

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, bfs(r, c))
        return res