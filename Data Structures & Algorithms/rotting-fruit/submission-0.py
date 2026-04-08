from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten_oranges = deque()
        fresh_oranges, minutes = 0, 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rotten_oranges and fresh_oranges > 0:
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()
                
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        rotten_oranges.append((row, col))
                        fresh_oranges -= 1
            minutes += 1
        return minutes if fresh_oranges == 0 else -1
