class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.buckets = [ListNode(-1) for _ in range(1_000)]

    def _hash(self, key: int) -> int:
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.nxt:
            if curr.nxt.key == key:
                return
            curr = curr.nxt
        curr.nxt = ListNode(key)


    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt

    def contains(self, key: int) -> bool:
        curr = self.buckets[self._hash(key)]
        while curr.nxt:
            if curr.nxt.key == key:
                return True
            curr = curr.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)