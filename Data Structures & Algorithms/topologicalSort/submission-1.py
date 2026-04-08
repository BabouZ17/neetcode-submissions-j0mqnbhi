from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjs = defaultdict(list)

        for u, v in edges:
            adjs[u].append(v)

        topSort = []
        visited = set()
        visiting = set()

        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False

            visiting.add(i)
            for nei in adjs[i]:
                if not dfs(nei):
                    return False

            visited.add(i)
            visiting.remove(i)
            topSort.append(i)
            return True
        
        for i in range(n):
            if not dfs(i):
                return list()

        topSort.reverse()
        return topSort