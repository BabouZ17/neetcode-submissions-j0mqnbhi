import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjs = dict()
        for i in range(n):
            adjs[i] = list()

        for s, d, w in edges:
            adjs[s].append((d, w))

        shortest = dict()
        heap = [(0, src)]

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adjs[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(heap, (w1 + w2, n2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest