from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr == ROWS or
                        nc == COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == "0"
                    ):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands      