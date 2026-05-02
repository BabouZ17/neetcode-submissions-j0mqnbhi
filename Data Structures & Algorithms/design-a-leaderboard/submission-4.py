import heapq
from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.players = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.players.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.players[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
