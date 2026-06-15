class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        duplicates = set()
        seen = set()

        curr = head
        while curr:
            if curr.val in seen:
                duplicates.add(curr.val)
            
            seen.add(curr.val)
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val in duplicates:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next