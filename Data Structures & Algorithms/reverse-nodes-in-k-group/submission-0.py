# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy   # tail of the previously reversed group

        curr = head
        for i in range(count//k):
            prev = None
            node = curr
            for _ in range(k):
                count += 1
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            group_prev.next = prev   # link previous group's tail to this group's new head
            node.next = curr         # link this group's tail to the next unprocessed node
            group_prev = node        # this group's tail becomes the next "group_prev"
        return dummy.next
            