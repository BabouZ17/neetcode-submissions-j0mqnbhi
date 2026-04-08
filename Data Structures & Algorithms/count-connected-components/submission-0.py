class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pars = [i for i in range(n)]
        ranks = [1] * n

        total_components = n

        def find(x: int):
            if x != pars[x]:
                pars[x] = find(pars[x])
            return pars[x]

        def union(n1: int, n2: int):
            nonlocal total_components
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return

            if ranks[p1] > ranks[p2]:
                pars[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                pars[p1] = p2
                ranks[p2] += ranks[p1]
            total_components -= 1

        for src, dst in edges:
            union(src, dst)

        return total_components