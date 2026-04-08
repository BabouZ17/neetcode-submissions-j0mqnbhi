class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, node: int):
        curr = node
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n

        for src, dst in edges:
            if dsu.union(src, dst):
                res -= 1
        return res