# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        result = dummy

        heap = []
        heapq.heapify(heap)

        for lkd in lists:
            curr = lkd
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        while len(heap) > 0:
            val = heapq.heappop(heap)
            result.next = ListNode(val)
            result = result.next

        return dummy.next
