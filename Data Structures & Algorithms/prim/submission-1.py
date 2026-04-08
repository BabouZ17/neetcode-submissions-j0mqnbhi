import heapq
from collections import defaultdict

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjs = defaultdict(list)
        for src, dst, cost in edges:
            adjs[src].append((dst, cost))
            adjs[dst].append((src, cost))

        total = 0
        visited = set()

        heap = [(0, 0)]

        while heap and len(visited) < n:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            total += cost

            for nei, cost in adjs[node]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))
        return total if len(visited) == n else -1