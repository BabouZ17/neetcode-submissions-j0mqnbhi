import heapq
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = list()

        for grade in self.scores.values():
            heapq.heappush(heap, grade)
            if len(heap) > K:
                heapq.heappop(heap)

        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
