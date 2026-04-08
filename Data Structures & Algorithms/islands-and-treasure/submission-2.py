from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        distance = 0
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                print(r,c)
                grid[r][c] = distance
                for dr, dc in drs:
                    if (
                        min(r+dr,c+dc) < 0
                        or r+dr == ROWS
                        or c+dc == COLS
                        or (r+dr,c+dc) in visited
                        or grid[r+dr][c+dc] == -1
                    ):
                        continue
                    visited.add((r+dr,c+dc))
                    q.append((r+dr,c+dc))
            distance += 1
                
