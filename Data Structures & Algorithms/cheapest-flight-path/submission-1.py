from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for s, d, p in flights:
            adj[s].append((d, p))

        queue = deque([(0, src, 0)]) # cost, source, stops
        while queue:
            cost, node, stops = queue.popleft()
            if stops > k:
                continue
            
            for nei, w in adj[node]:
                nextCost = cost + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    queue.append((nextCost, nei, stops + 1))
        return prices[dst] if prices[dst] != float("inf") else -1