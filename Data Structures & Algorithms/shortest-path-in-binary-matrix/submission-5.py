from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))

        while queue:
            r, c, length = queue.popleft()

            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) < 0 or
                    nr == N or
                    nc == N or
                    grid[nr][nc] or
                    (nr, nc) in visited
                ):
                    continue
                queue.append((nr, nc, length + 1))
                visited.add((nr, nc))
        return -1
            