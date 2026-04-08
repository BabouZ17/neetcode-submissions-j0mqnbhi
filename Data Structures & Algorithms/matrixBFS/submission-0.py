from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        queue.append((0, 0))

        visited = set()
        visited.add((0, 0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in drs:
                    row, col = r + dr, c + dc
                    if (
                        min(row, col) < 0
                        or row == ROWS
                        or col == COLS
                        or (row, col) in visited
                        or grid[row][col] == 1
                    ):
                        continue
                    queue.append((row, col))
                    visited.add((row, col))
            length += 1

        return -1