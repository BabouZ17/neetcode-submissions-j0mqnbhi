from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([(0, 0, 0)])
        visited = set((0, 0))

        while queue:
            r, c, length = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))

        return -1