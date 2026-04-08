# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while curr and curr.next:
            while curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next

        return dummy.next