from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.computeDistance(point), point) for point in points]
        heapq.heapify(heap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        
    def computeDistance(self, point: List[int]) -> float:
        return sqrt(point[0]**2 + point[1]**2)