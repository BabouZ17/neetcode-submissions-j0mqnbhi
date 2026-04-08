from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = defaultdict(int)
        outdegrees = defaultdict(int)

        for a, b in trust:
            indegrees[b] += 1
            outdegrees[a] += 1
        
        for i in range(1, n + 1):
            if outdegrees[i] == 0 and indegrees[i] == n - 1:
                return i
        return -1