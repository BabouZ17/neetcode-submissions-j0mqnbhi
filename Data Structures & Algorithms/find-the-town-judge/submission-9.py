class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outtrusts = defaultdict(int)
        inttrusts = defaultdict(int)

        for src, dst in trust:
            inttrusts[dst] += 1
            outtrusts[src] += 1

        for i in range(1, n+1):
            if not outtrusts[i] and inttrusts[i] == n-1:
                return i
        return -1