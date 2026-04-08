class HashTable:
    
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity is too low")
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]
    
    def insert(self, key: int, value: int) -> None:
        hash_key = hash(key) % self.capacity
        bucket = self.buckets[hash_key]

        found_key = False
        for index, item in enumerate(bucket):
            item_key, item_val = item

            if key == item_key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
        
        if self.getSize() / self.getCapacity() >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        hash_key = hash(key) % self.capacity
        bucket = self.buckets[hash_key]

        found_key = False
        for index, item in enumerate(bucket):
            item_key, item_val = item

            if key == item_key:
                found_key = True
                break
        
        if found_key:
            return bucket[index][1]
        else:
            return -1

    def remove(self, key: int) -> bool:
        hash_key = hash(key) % self.capacity
        bucket = self.buckets[hash_key]

        found_key = False
        for index, item in enumerate(bucket):
            item_key, item_val = item

            if key == item_key:
                found_key = True
                break
        
        if found_key:
            bucket.pop(index)
            return True
        else:
            return False

    def getSize(self) -> int:
        return sum([len(bucket) for bucket in self.buckets if len(bucket) != 0])

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.buckets += [[] for _ in range(self.capacity)]
        self.capacity *= 2

