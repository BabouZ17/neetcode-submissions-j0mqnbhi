from collections import defaultdict
import heapq

class Leaderboard:

    def __init__(self):
        self.players = defaultdict(int) # map playerId to their score

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.players.values()))

    def reset(self, playerId: int) -> None:
        del self.players[playerId]
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
