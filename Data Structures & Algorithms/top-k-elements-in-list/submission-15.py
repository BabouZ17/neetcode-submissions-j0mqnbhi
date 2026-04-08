import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = list()
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        for key, val in freqs.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]