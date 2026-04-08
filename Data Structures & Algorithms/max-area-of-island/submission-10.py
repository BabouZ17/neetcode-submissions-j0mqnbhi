from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        area = 0

        def bfs(r, c):
            current_area = 1
            queue = deque([(r, c)])
            grid[r][c] = 0

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
                    grid[nr][nc] = 0
                    current_area += 1
                    queue.append((nr, nc))

            return current_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    area = max(area, bfs(r, c))

        return area
