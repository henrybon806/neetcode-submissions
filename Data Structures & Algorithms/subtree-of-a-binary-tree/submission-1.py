# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None or root.val != subRoot.val:
                return False
            return same(root.left, subRoot.left) and same(root.right, subRoot.right) 
        def recurse(root, subRoot):
            if same(root, subRoot):
                return True
            if root is None:
                return False
            return recurse(root.left, subRoot) or recurse(root.right, subRoot)
        return recurse(root, subRoot)