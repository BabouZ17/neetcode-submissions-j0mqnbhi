class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjs = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjs[i].append([dist, j])
                adjs[j].append([dist, i])

        res = 0
        visited = set()
        heap = [(0, 0)]
        while len(visited) < N:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            for cost, nei in adjs[i]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))
        return res