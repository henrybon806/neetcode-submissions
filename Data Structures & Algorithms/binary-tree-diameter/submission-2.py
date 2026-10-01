# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def recurse(root):
            if root is None:
                return 0
            return 1 + max(recurse(root.left), recurse(root.right))
        return max(recurse(root.left) + recurse(root.right), self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))