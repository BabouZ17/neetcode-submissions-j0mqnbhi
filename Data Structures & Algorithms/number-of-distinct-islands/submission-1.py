class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c, direction):
            if (
                not 0 <= r < len(grid) or
                not 0 <= c < len(grid[0]) or
                (r, c) in visited or
                not grid[r][c]
            ):
                return

            visited.add((r, c))
            path.append(direction)
            dfs(r + 1, c, "D")
            dfs(r - 1, c, "U")
            dfs(r, c + 1, "R")
            dfs(r, c - 1, "L")
            path.append("0")

        visited = set()
        unique_islands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                path = []
                dfs(r, c, "0")
                if path:
                    unique_islands.add(tuple(path))
        return len(unique_islands)
