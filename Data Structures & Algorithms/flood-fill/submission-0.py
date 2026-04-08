class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, prev_color):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                image[r][c] != prev_color
            ):
                return

            visited.add((r, c))
            prev_color = image[r][c]
            image[r][c] = color
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, prev_color)
        
        dfs(sr, sc, image[sr][sc])
        return image