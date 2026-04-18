class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(1_000)]

    def hash(self, key: int) -> int:
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        hashed = self.hash(key)
        if key not in self.buckets[hashed]:
            self.buckets[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = self.hash(key)
        if key in self.buckets[hashed]:
            self.buckets[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = self.hash(key)
        return key in self.buckets[hashed]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)