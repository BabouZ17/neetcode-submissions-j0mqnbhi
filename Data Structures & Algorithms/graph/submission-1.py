class Graph:
    
    def __init__(self):
        self.adjs = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjs:
            self.adjs[src] = set()
        if dst not in self.adjs:
            self.adjs[dst] = set()

        self.adjs[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjs and dst in self.adjs[src]:
            self.adjs[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())

    def dfs(self, src: int, dst: int, visited: set[int]) -> bool:
        if src in visited:
            return False

        if src == dst:
            return True

        visited.add(src)
        for nei in self.adjs[src]:
            if self.dfs(nei, dst, visited):
                return True
        return False
