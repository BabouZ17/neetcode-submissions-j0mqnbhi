# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        k %= n
        curr = head
        for i in range(n-k, n):
            curr.val = arr[i]
            curr = curr.next

        for i in range(n-k):
            curr.val = arr[i]
            curr = curr.next
        return head