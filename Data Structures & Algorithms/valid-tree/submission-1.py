from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adjs = defaultdict(list)
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        visited = set()
        visited.add(0)
        queue = deque([(0, -1)])

        while queue:
            node, prev_node = queue.popleft()

            for nei in adjs[node]:
                if nei == prev_node:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, node))
                visited.add(nei)

        return len(visited) == n