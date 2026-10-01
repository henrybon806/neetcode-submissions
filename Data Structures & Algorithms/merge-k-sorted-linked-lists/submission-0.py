# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode()
        head = merged
        count = {}

        for i in lists:
            while i:
                count[i.val] = count.get(i.val, 0) + 1
                i = i.next
        for key in sorted(count.keys()):
            for i in range(count[key]):
                merged.next = ListNode(key)
                merged = merged.next
        return head.next
