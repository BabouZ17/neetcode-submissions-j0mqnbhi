import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjs = defaultdict(list)

        for edge, prob in zip(edges, succProb):
            adjs[edge[0]].append([prob, edge[1]])
            adjs[edge[1]].append([prob, edge[0]])

        heap = [(-1, start_node)]
        visited = set()

        while heap:
            p1, n1 = heapq.heappop(heap)
            visited.add(n1)

            if n1 == end_node:
                return -p1
            
            for p2, n2 in adjs[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (p1*p2, n2))
        return 0.0