import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.distance(x, y), x, y) for (x, y) in points]
        heapq.heapify(heap)
    
        res = list()
        for _ in range(k):
            res.append(heapq.heappop(heap)[1:])
        return res

    @staticmethod
    def distance(x: int, y: int) -> float:
        return (x**2 + y**2)**0.5