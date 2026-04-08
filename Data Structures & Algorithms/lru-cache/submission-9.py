class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node: ListNode) -> None:
        prev, nxt = self.left, self.left.next
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = ListNode(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self._remove(lru)
            del self.cache[lru.key]
