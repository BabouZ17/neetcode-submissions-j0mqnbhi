# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        vals = []
        while stack1 and stack2:
            new_val = stack1.pop() + stack2.pop() + carry
            carry, remainder = divmod(new_val, 10)
            vals.append(remainder)

        while stack1:
            new_val = stack1.pop() + carry
            carry, remainder = divmod(new_val, 10)
            vals.append(remainder)

        while stack2:
            new_val = stack2.pop() + carry
            carry, remainder = divmod(new_val, 10)
            vals.append(remainder)

        if carry:
            vals.append(carry)       

        dummy = ListNode(-1)
        curr = dummy
        while vals:
            curr.next = ListNode(vals.pop())
            curr = curr.next
        return dummy.next