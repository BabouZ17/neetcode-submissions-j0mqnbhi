class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
        self.number_of_components = n

    def find(self, x: int) -> int:
        if x!= self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parents[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parents[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.number_of_components -= 1
            return True
        return False

    def getNumComponents(self) -> int:
        return self.number_of_components