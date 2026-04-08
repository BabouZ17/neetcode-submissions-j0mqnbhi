class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        prev = self.head.next
        new_node.next = prev
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr and curr.next:
            curr = curr.next

        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while curr and index > i:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        values = list()
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
