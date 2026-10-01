# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        output = []
        while queue:
            size = len(queue)
            out = []
            for i in range(size):
                curr = queue.pop(0)
                if curr is not None:
                    out.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            output.append(out)
        return output[:-1]