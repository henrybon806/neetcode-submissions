# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next   # save before overwriting
            curr.next = prev        # reverse the pointer
            prev = curr             # advance prev
            curr = next_node        # advance curr
        return prev
