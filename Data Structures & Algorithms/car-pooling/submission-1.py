import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        distance = 0
        for c, f, t in trips:
            heapq.heappush(heap, (f, t, c))
        
        current_capacity = capacity
        destination = -1

        while heap:
            from_, to, next_cap = heapq.heappop(heap)
            if from_ >= destination:
                current_capacity = capacity

            if current_capacity < next_cap:
                return False
            else:
                current_capacity -= next_cap
            
            distance = from_
            destination = to

        return True