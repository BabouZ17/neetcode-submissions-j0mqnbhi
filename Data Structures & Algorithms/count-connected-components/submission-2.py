class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjs = [[] for _ in range(n)]
        visited = [False] * n

        for src, dst in edges:
            adjs[src].append(dst)
            adjs[dst].append(src)

        def dfs(node):
            for nei in adjs[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res