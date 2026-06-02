from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjs = defaultdict(list)
        for par, child in edges:
            adjs[par].append(child)
            adjs[child].append(par)

        def dfs(curr, par):
            time = 0
            for child in adjs[curr]:
                if child == par:
                    continue
                child_time = dfs(child, curr)
                if child_time > 0 or hasApple[child]:
                    time += 2 + child_time
            return time
        return dfs(0, -1)