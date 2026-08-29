class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.nxt = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
    
    def getPrev(self, index: int) -> ListNode:
        curr = self.head
        while curr and index:
            curr = curr.nxt
            index -= 1
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).nxt.val

    def insertAtIndex(self, val: int, index: int) -> None:
        if index > self.size:
            return

        prev = self.getPrev(index)
        node = ListNode(val)
        nxt = prev.nxt
        node.nxt = nxt
        prev.nxt = node
        self.size += 1

    def insertHead(self, val: int) -> None:
        self.insertAtIndex(val, 0)

    def insertTail(self, val: int) -> None:
        self.insertAtIndex(val, self.size)

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        prev = self.getPrev(index)
        prev.nxt = prev.nxt.nxt
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.nxt
        while curr:
            vals.append(curr.val)
            curr = curr.nxt
        return vals
