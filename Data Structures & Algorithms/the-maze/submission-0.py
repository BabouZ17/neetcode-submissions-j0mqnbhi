class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(r: int, c: int):
            if (r, c) == tuple(destination):
                return True
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                
                stopping_r, stopping_c = nr - dr, nc - dc
                if dfs(stopping_r, stopping_c): return True
            return False


        return dfs(start[0], start[1])