import heapq
from math import sqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k:
            g = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(g)))
            k -= 1
        return -sum(gifts)