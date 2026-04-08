import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        counts = {}

        heap = list()
        heapq.heapify(heap)

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for val, count in counts.items():
            heapq.heappush(heap, (-1 * count, val))
        
        res = list()
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res
            

                