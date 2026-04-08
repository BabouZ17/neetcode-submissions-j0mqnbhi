import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, -1 * (y - x))    
        return -heapq.heappop(heap) if len(heap) > 0 else 0