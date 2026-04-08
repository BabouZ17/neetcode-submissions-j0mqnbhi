import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = defaultdict(list)

        for u, v, t in times:
            adjs[u].append((t, v))

        heap = [(0, k)]
        visited = set()
        t = 0

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
                
            visited.add(n1)
            t = t1

            for t2, n2 in adjs[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (t + t2, n2))


        return t if len(visited) == n else -1