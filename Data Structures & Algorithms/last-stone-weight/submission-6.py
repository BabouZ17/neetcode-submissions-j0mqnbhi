import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-1 * stone for stone in stones]
        heapq.heapify(self.heap)

        while len(self.heap) > 1:
            y, x = -1 * heapq.heappop(self.heap), -1 * heapq.heappop(self.heap)

            if x < y:
                heapq.heappush(self.heap, -1 * (y - x))    
        return -1 * heapq.heappop(self.heap) if len(self.heap) > 0 else 0