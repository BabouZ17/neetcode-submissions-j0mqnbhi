import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        heap = [(-val, key) for key, val in freqs.items()]
        heapq.heapify(heap)
        
        res = list()
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res