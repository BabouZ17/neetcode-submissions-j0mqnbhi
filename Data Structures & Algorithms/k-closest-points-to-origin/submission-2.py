import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.distance(x, 0, y, 0), x, y) for (x, y) in points]
        heapq.heapify(heap)
    
        res = list()
        for _ in range(k):
            res.append(heapq.heappop(heap)[1:])
        return res

    @staticmethod
    def distance(x1: int, x2: int, y1: int, y2: int) -> float:
        return ((x1-x2)**2 + (y1-y2)**2)**0.5