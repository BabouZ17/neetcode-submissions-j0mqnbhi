# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        result = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_value = l1.val if l1 is not None else 0
            l2_value = l2.val if l2 is not None else 0
            value = l1_value + l2_value + carry
            
            carry, node_val = divmod(value, 10)
            result.next = ListNode(node_val)
            
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next