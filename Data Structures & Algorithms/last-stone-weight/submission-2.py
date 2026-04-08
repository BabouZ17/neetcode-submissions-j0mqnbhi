import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_a, stone_b = -heapq.heappop(heap), -heapq.heappop(heap)
            print(stone_a, stone_b)
            if stone_a == stone_b:
                continue
            if stone_a > stone_b:
                left_stone = stone_a - stone_b
                heapq.heappush(heap, -left_stone)
        return -heap[0] if heap else 0