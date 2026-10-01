# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        output = []
        while queue:
            size = len(queue)
            if queue[-1] is not None:
                output.append(queue[-1].val)
            for i in range(size):
                curr = queue.pop(0)
                if curr is not None:
                    if curr.left is not None:
                        queue.append(curr.left)
                    if curr.right is not None:
                        queue.append(curr.right)
        return output

