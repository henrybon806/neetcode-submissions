# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root, minv, maxv):
            if root is None:
                return True
            if root.val <= minv or root.val >= maxv:
                return False
            return recurse(root.left, minv, root.val) and recurse(root.right, root.val, maxv)

        return recurse(root, -1000000001, 1000000001)