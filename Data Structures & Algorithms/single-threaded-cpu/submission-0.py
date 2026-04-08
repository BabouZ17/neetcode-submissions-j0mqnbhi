import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        available = []
        pending = []
        time = 0
        
        for i, (enqueingTime, processingTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueingTime, processingTime, i))

        while available or pending:
            while pending and pending[0][0] <= time:
                enqueingTime, processingTime, idx = heapq.heappop(pending)
                heapq.heappush(available, (processingTime, idx))

            if not available:
                time = pending[0][0]
                continue
            
            processingTime, idx = heapq.heappop(available)
            time += processingTime
            res.append(idx)
        return res