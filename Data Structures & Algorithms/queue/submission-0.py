class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = self.next = None

class Deque:
    
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next, self.right.prev = self.right, self.left

    def isEmpty(self) -> bool:
        return self.left.next.val == self.right.val

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = new_node
        new_node.prev, new_node.next = prev, nxt
        self.printall()

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        prev, nxt = self.left, self.left.next
        prev.next = nxt.prev = new_node
        new_node.prev, new_node.next = prev, nxt
        self.printall()
        
    def printall(self):
        curr = self.left.next
        while curr:
            print(curr.val)
            curr = curr.next

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        self.printall()

        value = self.right.prev.val
        prev, nxt = self.right.prev.prev, self.right
        prev.next, nxt.prev = nxt, prev
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        self.printall()
        value = self.left.next.val
        prev, nxt = self.left, self.left.next.next
        prev.next, nxt.prev = nxt, prev
        return value
