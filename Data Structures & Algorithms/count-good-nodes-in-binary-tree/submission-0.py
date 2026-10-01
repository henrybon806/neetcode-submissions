# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0
        def recurse(root, val):
            if root is None:
                return
            if val is None:
                val = root.val
            if root.val >= val:
                self.total += 1
            maxval = max(root.val, val)
            recurse(root.left, maxval)
            recurse(root.right, maxval)
        recurse(root, None)
        return self.total