from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        queue = deque()

        for i, t in enumerate(tickets):
            queue.append((t, True if i == k else False))

        while queue:
            tickets, isPerson = queue.popleft()
            tickets -= 1
            time += 1
            if tickets:
                queue.append((tickets, isPerson))
            elif isPerson:
                break
        return time


        