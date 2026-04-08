from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()

        time = 0
        fruits = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruits += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fruits > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fruits -= 1

            time += 1
        return time if fruits == 0 else -1