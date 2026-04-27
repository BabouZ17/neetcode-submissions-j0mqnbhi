from collections import deque
class Solution:
    def normalize(self, coords: set(tuple), start_r: int, start_c: int) -> tuple[int, int]:
        relative_shape = []
        for r, c in coords:
            relative_shape.append((r - start_r, c - start_c))
        relative_shape.sort()
        return tuple(relative_shape)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        all_visited = set()
        directions = [[0, 1], [0, -1], [1,0], [-1, 0]]

        def bfs(r, c) -> set():
            queue = deque([(r, c)])
            visited = {(r, c)}
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < ROWS and
                            0 <= nc < COLS and
                            (nr, nc) not in visited and
                            grid[nr][nc]
                        ):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            return visited

        shapes = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in all_visited:
                    visited = bfs(r, c)
                    all_visited.update(visited)
                    
                    visited = self.normalize(visited, r, c)
                    shapes.add(visited)

        # find islands
        return len(shapes)