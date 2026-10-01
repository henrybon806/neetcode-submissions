"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copies = {}
        node = head
        copy = Node(node.val)
        copies[node] = copy
        chead = copy
        while node.next:
            copy.next = Node(node.next.val)
            copies[node.next] = copy.next
            copy = copy.next
            node = node.next
        node = head
        copy = chead
        while node:
            if node.random is not None:
                copy.random = copies[node.random]
            else:
                copy.random = None
            copy = copy.next
            node = node.next
        return chead
