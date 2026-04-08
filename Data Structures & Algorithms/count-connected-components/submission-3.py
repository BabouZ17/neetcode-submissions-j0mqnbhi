from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjs = [[] for _ in range(n)]
        visited = [False] * n
        for src, dst in edges:
            adjs[src].append(dst)
            adjs[dst].append(src)

        def bfs(node):
            queue = deque([node])
            visited[node] = True
            while queue:
                node = queue.popleft()
                for nei in adjs[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                res += 1
        return res