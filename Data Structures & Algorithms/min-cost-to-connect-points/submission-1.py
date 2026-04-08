class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n+1))
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res