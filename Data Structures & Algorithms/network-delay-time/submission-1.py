import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = dict()
        for i in range(1, n + 1):
            adjs[i] = list()

        for ui, vi, ti in times:
            adjs[ui].append((vi, ti))

        heap = [(0, k)]
        shortest = dict()
        total_time = 0

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            total_time = t1
            shortest[n1] = t1

            for n2, t2 in adjs[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (t1 + t2, n2))
        
        return total_time if len(shortest) == n else -1