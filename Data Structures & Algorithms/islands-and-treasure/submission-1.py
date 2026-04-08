from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        q = deque()

        def add(r,c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visited
                or grid[r][c] == -1
            ):
                return
            visited.add((r,c))
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                add(r+1, c)
                add(r-1, c)
                add(r, c+1)
                add(r, c-1)
            distance += 1
                
