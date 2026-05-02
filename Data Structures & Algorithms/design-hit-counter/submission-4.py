class HitCounter:

    def __init__(self):
        self.capacity = 300
        self.buckets = [[0, 0] for _ in range(self.capacity)] # timestamp, count

    def hit(self, timestamp: int) -> None:
        key = timestamp % self.capacity
        if self.buckets[key][0] == timestamp:
            self.buckets[key][1] += 1
        else:
            self.buckets[key][0] = timestamp
            self.buckets[key][1] = 1

    def getHits(self, timestamp: int) -> int:
        hits = 0

        for tmp, cnt in self.buckets:
            if tmp > 0 and timestamp - tmp < 300:
                hits += cnt
        return hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
