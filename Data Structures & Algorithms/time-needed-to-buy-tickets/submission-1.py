from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        queue = deque()
        n = len(tickets)

        for i in range(n):
            queue.append(i)

        while queue:
            time += 1
            curr = queue.popleft()
            tickets[curr] -= 1
            if tickets[curr] == 0:
                if curr == k:
                    return time
            else:
                queue.append(curr)
        return time


        