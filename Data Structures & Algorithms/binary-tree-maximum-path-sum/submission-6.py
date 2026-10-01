# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = -float('inf')
        def recurse(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                self.best = max(self.best, root.val)
                return root.val
            elif root.left is None:
                right = recurse(root.right)
                self.best = max(self.best, right, right+root.val, root.val)
                return max(root.val + right, root.val)
            elif root.right is None:
                left = recurse(root.left)
                self.best = max(self.best, left, left+root.val, root.val)
                return max(root.val + left, root.val)
            left = recurse(root.left)
            right = recurse(root.right)
            bend = max(left+right+root.val, right+root.val, left+root.val)
            self.best = max(self.best, bend, left, right, root.val)
            return root.val + max(0, left, right)
        recurse(root) 
        return self.best