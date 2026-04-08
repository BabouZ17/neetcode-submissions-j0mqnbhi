from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        directions = [
            [1, 0], [-1, 0], [0, 1],
            [0, -1], [1, 1], [-1, 1],
            [1, -1], [-1, -1]
        ]
        visited = set((0, 0))
        queue = deque([(0, 0, 1)])
        
        while queue:
            r, c, length = queue.popleft()

            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N and
                    0 <= nc < N and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))

        return -1