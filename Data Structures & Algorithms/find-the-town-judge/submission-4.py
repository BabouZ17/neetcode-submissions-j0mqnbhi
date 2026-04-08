from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingoing, outgoing = defaultdict(int), defaultdict(int)

        for src, dst in trust:
            ingoing[dst] += 1
            outgoing[src] += 1

        for i in range(1, n+1):
            if outgoing[i] == 0 and ingoing[i] == n - 1:
                return i
        return -1