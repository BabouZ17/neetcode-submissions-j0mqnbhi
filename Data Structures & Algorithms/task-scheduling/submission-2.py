import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)

        heap = [-val for val in c.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
             