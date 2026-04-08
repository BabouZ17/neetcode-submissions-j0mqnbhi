class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build DSU
        pars = [i for i in range(len(edges)+1)]
        ranks = [1] * (len(edges) +1)

        def find(n) -> int:
            if n != pars[n]:
                n = find(pars[n])
            return pars[n]
        
        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if ranks[p1] > ranks[p2]:
                pars[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                pars[p1] = p2
                ranks[p2] += ranks[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

