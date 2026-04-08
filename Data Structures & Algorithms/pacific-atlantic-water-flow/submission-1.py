class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, prev):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                heights[r][c] < prev
            ):
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        return list(atlantic.intersection(pacific))