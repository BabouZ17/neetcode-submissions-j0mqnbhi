import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_a, stone_b = heapq.heappop(heap), heapq.heappop(heap)
            if stone_b > stone_a:
                heapq.heappush(heap, stone_a - stone_b)
        
        heap.append(0)
        return abs(heap[0])