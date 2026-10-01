# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newNode = ListNode()
        head = newNode
        prev = None
        while l1 or l2:
            one = 0
            two = 0
            if l1:
                one = l1.val
                l1 = l1.next
            if l2:
                two = l2.val
                l2 = l2.next    
            newtotal = (one + two + carry) % 10
            carry = (one + two + carry) // 10   
            newNode.val = newtotal
            newNode.next = ListNode()
            prev = newNode
            newNode = newNode.next

        if carry > 0:
            newNode.val = carry
            prev = newNode
            newNode.next = ListNode()
            newNode = newNode.next

        prev.next = None
        return head
