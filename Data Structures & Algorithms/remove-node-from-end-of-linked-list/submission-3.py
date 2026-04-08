# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        i = n
        left = dummy
        right = head
        while i > 0:
            right = right.next
            i -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
