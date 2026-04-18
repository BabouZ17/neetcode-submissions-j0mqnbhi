class HitCounter:

    def __init__(self):
        self.buckets = [[0, 0] for _ in range(300)] # timestamp, count

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300

        if self.buckets[idx][0] != timestamp:
            self.buckets[idx][0] = timestamp
            self.buckets[idx][1] = 1
        else:
            self.buckets[idx][1] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.buckets[i][0] < 300:
                total += self.buckets[i][1]
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
