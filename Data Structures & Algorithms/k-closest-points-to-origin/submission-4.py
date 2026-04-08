import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.distance(point[0], point[1]), point) for point in points]        
        heapq.heapify(heap)

        res = list()
        while k > 0:
            k -= 1
            res.append(heapq.heappop(heap)[1])
        return res

    def distance(self, x: int, y: int) -> float:
        return (x**2 + y**2)**0.5