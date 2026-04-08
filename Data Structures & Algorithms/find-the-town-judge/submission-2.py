class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingoing = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            ingoing[dst] += 1

        for i in range(1, n+1):
            if outgoing[i] == 0 and ingoing[i] == n - 1:
                return i
        return -1