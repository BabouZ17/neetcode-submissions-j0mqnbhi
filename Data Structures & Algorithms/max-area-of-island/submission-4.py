from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            current_area = 1
            queue = deque()
            queue.append((r, c))
            visited.add((r,c))

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr == ROWS or
                        nc == COLS or
                        grid[nr][nc] == 0 or
                        (nr, nc) in visited
                    ):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    current_area += 1
            return current_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area