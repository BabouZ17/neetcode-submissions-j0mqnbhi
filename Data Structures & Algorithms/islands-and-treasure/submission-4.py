from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c, distance = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == INF
                    ):
                        queue.append((nr, nc, distance + 1))
                        visited.add((nr, nc))
                        grid[nr][nc] = distance + 1