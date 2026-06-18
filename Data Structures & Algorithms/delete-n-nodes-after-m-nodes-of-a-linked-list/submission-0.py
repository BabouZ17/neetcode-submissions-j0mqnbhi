# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current_node = head
        last_m_node = head

        while current_node:
            m_count, n_count = m, n

            while current_node and m_count != 0:
                last_m_node = current_node
                current_node = current_node.next

                m_count -= 1

            while current_node and n_count != 0:
                current_node = current_node.next
                n_count -= 1

            last_m_node.next = current_node

        return head