class ListNode:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)        
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node: ListNode):
        prev, nxt = self.head, self.head.next
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def _remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])        

        node = ListNode(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
