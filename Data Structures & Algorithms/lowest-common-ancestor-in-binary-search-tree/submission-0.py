# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(root, p, q):
            if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
                return root
            elif root.val > p.val and root.val > q.val:
                return recurse(root.left, p, q)
            else:
                return recurse(root.right, p, q)
        return recurse(root, p, q)
