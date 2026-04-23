class ListNode:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.nxt = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, ListNode] = dict()
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def _add(self, node: ListNode):
        prev, nxt = self.head, self.head.nxt
        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node

    def _remove(self, node: ListNode):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to refresh the key
            # remove node from current position, then append at head
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = ListNode(key=key, val=value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            last_node = self.tail.prev
            self._remove(last_node)
            del self.cache[last_node.key]

