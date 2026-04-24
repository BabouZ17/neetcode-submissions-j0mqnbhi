class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)] # list of list of key, val

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)
        found = False

        for i, pair in enumerate(self.buckets[idx]):
            if pair[0] == key:
                self.buckets[idx][i][1] = value
                found = True
                break
        
        if not found:
            self.buckets[idx].append([key, value])
            self.size += 1

        if self.shouldResize():
            self.resize()

    def shouldResize(self) -> bool:
        return self.size / self.capacity >= 0.5

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for i, pair in enumerate(self.buckets[idx]):
            if pair[0] == key:
                return self.buckets[idx][i][1]
        return -1

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        for i, pair in enumerate(self.buckets[idx]):
            if pair[0] == key:
                self.buckets[idx].pop(i)
                self.size -= 1
                return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old = self.buckets[:]
        self.capacity = 2 * self.capacity
        self.size = 0
        self.buckets = [[] for i in range(self.capacity)]

        for bucket in old:
            for key, val in bucket:
                self.insert(key, val)
