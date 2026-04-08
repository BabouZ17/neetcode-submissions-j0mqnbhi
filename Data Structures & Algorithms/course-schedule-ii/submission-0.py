from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjs = defaultdict(list)

        for a, b in prerequisites:
            adjs[a].append(b)

        topSort = []
        visited = set()
        visiting = set()

        def dfs(src: int) -> bool:
            if src in visiting:
                return False
            if src in visited:
                return True
            
            visiting.add(src)
            for nei in adjs[src]:
                if not dfs(nei):
                    return False
            
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort