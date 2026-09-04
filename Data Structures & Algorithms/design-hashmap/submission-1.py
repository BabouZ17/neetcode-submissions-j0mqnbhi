class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.nxt = None

class MyHashMap:

    def __init__(self):
        self.buckets = [ListNode(0, 0) for _ in range(10_000)]

    def _hash(self, key: int) -> int:
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt.val = value
                return
            curr = curr.nxt

        curr.nxt = ListNode(key, value)

    def get(self, key: int) -> int:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        while curr.nxt:
            if curr.nxt.key == key:
                return curr.nxt.val
            curr = curr.nxt
        return -1

    def remove(self, key: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt = curr.nxt.nxt
                return 
            curr = curr.nxt


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)