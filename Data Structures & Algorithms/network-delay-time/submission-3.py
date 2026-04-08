import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = defaultdict(list)

        for u, v, t in times:
            adjs[u].append((t, v))

        time = 0
        heap = [(0, k)]
        visited = set()

        while heap:
            t1, n1 = heapq.heappop(heap)

            if n1 in visited:
                continue
            visited.add(n1)

            time = t1

            for t2, n2 in adjs[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (t1 + t2, n2))
        return time if len(visited) == n else -1