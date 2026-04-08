# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            value = l1_val + l2_val + carry

            carry, node_val = divmod(value, 10)

            curr.next = ListNode(node_val)
            curr = curr.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if l1 is not None:
            curr.next = l1
            curr = curr.next
        if l2 is not None:
            curr.next = l2
            curr = curr.next

        return dummy.next