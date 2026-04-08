class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, original_color):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                image[r][c] != original_color
            ):
                return

            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc, original_color)
        
        dfs(sr, sc, image[sr][sc])
        return image