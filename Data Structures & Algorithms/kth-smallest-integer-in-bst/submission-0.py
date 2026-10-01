# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = k
        self.answer = None
        def recurse(root):
            if root is None:
                return
            recurse(root.left)
            self.counter -= 1
            if self.counter == 0:
                self.answer = root.val
            recurse(root.right)
        recurse(root)
        return self.answer