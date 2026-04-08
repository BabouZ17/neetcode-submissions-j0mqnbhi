from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjs = defaultdict(list)

        for crs, prev in prerequisites:
            adjs[crs].append(prev)

        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False

            if adjs[node] == []:
                return True
            
            visited.add(node)
            for nei in adjs[node]:
                if not dfs(nei):
                    return False
            
            visited.remove(node)
            adjs[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True