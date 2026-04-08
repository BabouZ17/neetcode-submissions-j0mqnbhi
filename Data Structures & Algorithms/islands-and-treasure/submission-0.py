from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        visited = set()

        def bfs(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visited
                or grid[r][c] == -1
            ):
                return
            visited.add((r,c))
            queue.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in drs:
                    bfs(r+dr, c+dc)
            dist += 1