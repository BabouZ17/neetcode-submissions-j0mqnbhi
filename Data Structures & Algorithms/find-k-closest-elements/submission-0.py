import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            heapq.heappush(heap, (abs(x - a), a))
        
        res = [] 
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        res.sort()
        return res