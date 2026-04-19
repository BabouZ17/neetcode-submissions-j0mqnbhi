class DSU:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        self.components -= 1
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parents[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parents[pu] = pv
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    dsu.union(i, j)
        return dsu.components
        