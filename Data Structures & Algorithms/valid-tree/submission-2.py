class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n+1))
        self.ranks = [1] * n
        self.comps = n

    def find(self, node: int):
        if self.parents[node] != node:
            self.parents[node] = self.parents[self.parents[node]]
        return self.parents[node]

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        self.comps -= 1
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        return True

    def components(self) -> int:
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1