from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            if grid[0][0] or grid[ROWS-1][COLS-1]:
                return -1


            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = deque()
            queue.append((0, 0))
            visited = set()
            visited.add((0, 0))
            length = 0

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
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
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                length += 1
            return -1
        return bfs(grid)