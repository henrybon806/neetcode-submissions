"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        head = root
        root.next = None
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if not curr:
                    continue
                q.append(curr.left)
                q.append(curr.right)
            while q and not q[-1]:
                q.pop()
            for i in range(len(q)):
                if i == len(q)-1:
                    q[i].next = None
                else:
                    q[i].next = q[i+1]
        return head

                

