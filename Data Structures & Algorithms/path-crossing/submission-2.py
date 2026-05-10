class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        directions = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        curr_path = (0, 0)
        visited = set()
        visited.add(curr_path)

        for direction in path:
            curr_path = (curr_path[0] + directions[direction][0], curr_path[1] + directions[direction][1])
            if curr_path in visited:
                return True
            visited.add(curr_path)
        return False