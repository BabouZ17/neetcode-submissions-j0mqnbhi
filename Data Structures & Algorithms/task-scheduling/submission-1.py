from collections import deque, defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)

        for task in tasks:
            freqs[task] = freqs[task] + 1
        
        heap = [-val for val in freqs.values()]
        heapq.heapify(heap)
        print(heap)

        time = 0
        q = deque()
        while heap or q:

            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            time += 1
        return time