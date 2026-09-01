class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(1_000)]

    def _hash(self, key: int) -> int:
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        hash_val = self._hash(key)
        if key not in self.buckets[hash_val]:
            self.buckets[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        if key in self.buckets[hash_val]:
            self.buckets[hash_val].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)