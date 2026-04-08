from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjs = defaultdict(list)
        for a, b in prerequisites:
            adjs[a].append(b)

        visited = set()

        def dfs(src):
            if src in visited:
                return False
            if adjs[src] == []:
                return True

            visited.add(src)
            for nei in adjs[src]:
                if not dfs(nei):
                    return False

            visited.remove(src)
            adjs[src] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True