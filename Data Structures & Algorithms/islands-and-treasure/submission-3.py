from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        def bfs():
            while queue:
                for _ in range(len(queue)):
                    r, c, i = queue.popleft()

                    i += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            nr in range(ROWS) and
                            nc in range(COLS) and
                            grid[nr][nc] == INF
                        ):
                            grid[nr][nc] = i
                            queue.append((nr, nc, i))
        bfs()