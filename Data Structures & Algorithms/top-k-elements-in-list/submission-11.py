import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = list()
        heap = list()
        heapq.heapify(heap)

        c = {}
        for num in nums:
            c[num] = c.get(num, 0) + 1

        for num, freq in c.items():
            heapq.heappush(heap, (-1 * freq, num))
        
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result