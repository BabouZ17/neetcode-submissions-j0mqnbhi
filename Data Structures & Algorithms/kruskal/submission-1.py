import heapq

class DSU:
    def __init__(self, n: int):
        self.pars = list(range(n+1))
        self.ranks = [1] * n

    def find(self, node: int) -> int:
        if self.pars[node] != node:
            self.pars[node] = self.find(self.pars[node])
        return self.pars[node]

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.ranks[p2] < self.ranks[p1]:
            self.pars[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.pars[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        heap = []
        res, components = 0, n - 1

        for u, v, w in edges:        
            heapq.heappush(heap, (w, u, v))

        while components > 0 and heap:
            cost, u, v = heapq.heappop(heap) 
            if dsu.union(u, v):
                res += cost
                components -= 1
        return res if components == 0 else -1