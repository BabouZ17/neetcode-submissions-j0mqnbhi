class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.prev = self.nxt = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        curr = self.head.nxt
        while curr and index:
            curr = curr.nxt
            index -= 1
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1        

    def addAtHead(self, val: int) -> None:
        nxt, prev = self.head.nxt, self.head
        node = ListNode(val)
        node.prev = prev
        node.nxt = nxt
        nxt.prev = node
        prev.nxt = node

    def addAtTail(self, val: int) -> None:
        nxt, prev = self.tail, self.tail.prev
        node = ListNode(val)
        node.prev = prev
        node.nxt = nxt
        nxt.prev = node
        prev.nxt = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.nxt
        while curr and index:
            curr = curr.nxt
            index -= 1
        
        if curr and index == 0:
            nxt, prev = curr, curr.prev
            node = ListNode(val)
            nxt.prev = node
            prev.nxt = node
            node.prev = prev
            node.nxt = nxt

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.nxt
        while curr and index:
            curr = curr.nxt
            index -= 1
        if curr and curr != self.tail and index == 0:
            nxt, prev = curr.nxt, curr.prev
            nxt.prev = prev
            prev.nxt = nxt


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)