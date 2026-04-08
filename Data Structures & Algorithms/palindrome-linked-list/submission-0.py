# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow2 = head
        left, right = list(), list()
        while slow:
            left.append(slow2.val)
            right.append(slow.val)
            slow2 = slow2.next
            slow = slow.next
        return left == right[::-1]
            