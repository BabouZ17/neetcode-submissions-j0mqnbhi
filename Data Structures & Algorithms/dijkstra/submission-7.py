import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjs = defaultdict(list)

        for u, v, w in edges:
            adjs[u].append((w, v))

        visited = {}
        heap = [(0, src)]

        while heap:
            w1, n1 = heapq.heappop(heap)

            if n1 in visited:
                continue
            visited[n1] = w1

            for w2, n2 in adjs[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))

        for i in range(n):
            if i not in visited:
                visited[i] = -1
        return visited