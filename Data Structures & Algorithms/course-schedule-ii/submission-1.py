from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjs = defaultdict(list)

        for a, b in prerequisites:
            adjs[a].append(b)

        top_sort = list()
        visited = set()
        visiting = set()

        def dfs(node: int) -> bool:
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for nei in adjs[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            top_sort.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return list()
        return top_sort