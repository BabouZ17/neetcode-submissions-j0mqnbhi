from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        visited = set()

        queue = deque([(0, 0, 1)])

        while queue:
            r, c, dist = queue.popleft()

            if r == N - 1 and c == N - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) < 0 or
                    nr == N or
                    nc == N or
                    (nr, nc) in visited or
                    grid[nr][nc]
                ):
                    continue
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))            

        return -1