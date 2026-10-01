# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        total = 0
        while count:
            total += 1
            count = count.next
        print(total)
        n = total - n
        counter = 0
        dummy = head
        if n == 0:
            return head.next
        while counter < n:
            print(dummy.val)
            counter += 1
            if counter == n:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head
        