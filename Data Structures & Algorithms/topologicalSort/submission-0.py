from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjs = defaultdict(list)

        for u, v in edges:
            adjs[u].append(v)

        topSort = []
        visited = set()
        visiting = set() # nodes being visited to detect cycles

        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in visiting:
                return False

            visiting.add(src)
            for nei in adjs[src]:
                if not dfs(nei):
                    return False # cycle

            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            return True

        for i in range(n):
            if not dfs(i):
                return [] # Return empty list in case of cycle
        
        topSort.reverse()
        return topSort