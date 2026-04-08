class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0
    
    def get_prev(self, index: int) -> ListNode:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        return self.get_prev(index).next.val

    def insertHead(self, val: int) -> None:
        self.insertAtIndex(0, val)

    def insertTail(self, val: int) -> None:
        self.insertAtIndex(self.size, val)

    def insertAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1

        node = ListNode(val)
        prev = self.get_prev(index)
        curr = prev.next
        prev.next = node
        node.next = curr
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        prev = self.get_prev(index)
        prev.next = prev.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        vals = list()
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next        
        return vals