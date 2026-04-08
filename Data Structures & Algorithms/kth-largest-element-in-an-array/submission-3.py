import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for num in nums:
            heapq.heappush(heap, -num)

        res = 0
        while k > 0:
            res = -heapq.heappop(heap)
            k -= 1
        return res