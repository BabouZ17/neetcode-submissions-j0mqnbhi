class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        curr = dummy

        remainder = 0
        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            new_val = val1 + val2 + remainder
            remainder, digit = divmod(new_val, 10)

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next