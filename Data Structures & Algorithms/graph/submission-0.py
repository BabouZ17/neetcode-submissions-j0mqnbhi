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
        if src not in self.adjs or dst not in self.adjs[src]:
            return False

        self.adjs[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        
        visited = set()
        return self._dfs(src, dst, visited)
    
    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True

        if src in visited:
            return False

        visited.add(src)
        for child in self.adjs[src]:
            if self._dfs(child, dst, visited):
                return True
        return False
