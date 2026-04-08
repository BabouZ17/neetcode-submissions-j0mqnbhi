import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        heap = [(0, 0, 0)] # cost, row, col

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) < 0 or
                    nr == ROWS or
                    nc == COLS or
                    (nr, nc) in visited
                ):
                    continue
                new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, (new_effort, nr, nc))