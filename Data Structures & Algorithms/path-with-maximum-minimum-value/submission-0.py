import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = [[False] * COLS for _ in range(ROWS)]
        visited[0][0] = True
        heap = [(-grid[0][0], 0, 0)]

        result = grid[0][0]
        while heap:
            val, r, c = heapq.heappop(heap)

            result = min(result, -val)

            if r == ROWS - 1 and c == COLS - 1:
                return result

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    not visited[nr][nc]
                ):
                    visited[nr][nc] = True
                    heapq.heappush(heap, (-grid[nr][nc], nr, nc))
