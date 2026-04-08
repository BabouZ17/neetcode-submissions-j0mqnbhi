from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        not grid[nr][nc]
                    ):
                        continue
                    area += 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    max_area = max(max_area, bfs(r, c))
        return max_area