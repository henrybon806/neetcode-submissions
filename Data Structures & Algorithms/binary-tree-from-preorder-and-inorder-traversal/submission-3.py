# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.idx = 0
        def recurse(start, end):
            if self.idx >= len(preorder) or start >= end:
                return None
            root = preorder[self.idx]
            self.idx += 1
            idx = pos[root]
            tree = TreeNode(root)
            tree.left = recurse(start, idx)
            tree.right = recurse(idx+1, end)
            return tree

        return recurse(0, len(inorder))