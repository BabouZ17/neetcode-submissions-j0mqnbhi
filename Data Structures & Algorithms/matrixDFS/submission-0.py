from typing import Set

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def helper(grid: List[List[int]], r: int, c: int, visited: Set[int]) -> int:
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or grid[r][c] == 1
            ):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visited.add((r,c))

            count = 0
            count += helper(grid, r + 1, c, visited)
            count += helper(grid, r - 1, c, visited)
            count += helper(grid, r, c - 1, visited)
            count += helper(grid, r, c + 1, visited)

            visited.remove((r,c))

            return count

        return helper(grid, 0, 0, set())