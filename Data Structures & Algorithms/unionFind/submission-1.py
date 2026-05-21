class UnionFind:
    
    def __init__(self, n: int):
        self.pairs = [i for i in range(n)]
        self.ranks = [0] * n
        self.num_of_components = n

    def find(self, x: int) -> int:
        if x != self.pairs[x]:
            self.pairs[x] = self.find(self.pairs[x])
        return self.pairs[x]     

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False

        if self.ranks[p1] < self.ranks[p2]:
            self.pairs[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        else:
            self.pairs[p2] = p1
            self.ranks[p1] += self.ranks[p2]
            
        self.num_of_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_of_components
