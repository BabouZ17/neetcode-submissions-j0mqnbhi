from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 1

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc]
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            return area

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visited:
                    area = max(area, bfs(r, c))
        return area