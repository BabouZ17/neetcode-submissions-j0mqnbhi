class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n + 1))
        self.ranks = [1] * (n+1)
    
    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        for u, v, w in edges:
            heapq.heappush(heap, (w, u, v))

        total = visited = 0
        dsu = DSU(n)

        while heap:
            weight, n1, n2 = heapq.heappop(heap)
            if not dsu.union(n1, n2):
                continue
            total += weight
            visited += 1
        return total if visited == n - 1 else -1